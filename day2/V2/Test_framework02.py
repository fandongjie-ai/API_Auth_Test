import jsonpath
import pytest
import requests,allure
from string import Template
from global_value import g_var
import os
from xToolkit import xfile

res = xfile.read("接口测试用例自动化.xlsx").excel_to_dict(sheet=0)

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

    print("打开Allure报告...")
    os.system("allure open ./report")