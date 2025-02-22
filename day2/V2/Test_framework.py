import jsonpath
import pytest
import requests,allure
from string import Template
from global_value import g_var
import os
from xToolkit import xfile
import openpyxl
import pandas as pd
# from xToolkit import xfile
# from hctest_excel_to.excel_to import Excel
#
# test_data_list = Excel("接口测试用例自动化.xlsx")
# print(test_data_list)
# test_data_list.sheet_name = "Sheet1"
# data = test_data_list.get_key_value_list_to_list(start=1)
# js_data = test_data_list.get_key_value_list_to_json(start=1)
# print("解析数据库".format(data))

# data = pd.read_excel("接口测试用例自动化.xlsx", sheet_name="Sheet1")
res = xfile.read("接口测试用例自动化.xlsx").excel_to_dict(sheet=0)
# print(res)
# res = data.to_dict(orient='records')
# 自动循环  DDT
@pytest.mark.parametrize("case_info", res)
def test_case_exec(case_info):

    url = case_info["接口URL"]
    dic = g_var().show_dict()
    if "$" in url:
        url = Template(url).substitute(dic)

    rep = requests.request(
        url=url,
        method=case_info["请求方式"],
        params=eval(case_info["URL参数"]),
        data=eval(case_info["JSON参数"]),
    )

    if case_info["提取参数"] != None or case_info["提取参数"] != "":
       lst = jsonpath.jsonpath(rep.json(), '$..' + case_info["提取参数"])
       g_var().set_dict(case_info["提取参数"], lst[0])


    assert rep.status_code == case_info["预期状态码"]
    print("测试用例执行成功")

if __name__ == '__main__':
    # 执行测试用例并生成 Allure 结果文件
    print("开始执行测试...")
    pytest.main([
        "-s", "-v",
        "--capture=sys",
        "Test_framework.py",
        "--clean-alluredir",
        "--alluredir=allure-results"
    ])
    print("测试结束")

    # 生成并打开 Allure 报告
    print("生成Allure报告...")
    os.system("allure generate allure-results -o report --clean")
    print("报告生成完成")



