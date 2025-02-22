import pytest
import requests
import os

from xToolkit import xfile
# from xToolkit import xfile
# from hctest_excel_to.excel_to import Excel
#
# test_data_list = Excel("接口测试用例自动化.xlsx")
# print(test_data_list)
# test_data_list.sheet_name = "Sheet1"
# data = test_data_list.get_key_value_list_to_list(start=1)
# js_data = test_data_list.get_key_value_list_to_json(start=1)
# print("解析数据库".format(data))

# file_path = os.path.join('day2', 'V1', '接口测试用例自动化.xlsx')
# print(file_path)

res = xfile.read("接口测试用例自动化.xlsx").excel_to_dict(sheet=0)
print(res)
# 自动循环  DDT
@pytest.mark.parametrize("case_info", res)
def test_case_exec(case_info):
    rep = requests.request(
        url=case_info["接口URL"],
        method=case_info["请求方式"],
        params=eval(case_info["URL参数"]),
        data=eval(case_info["JSON参数"]),
    )

    assert rep.status_code == case_info["预期状态码"]

if __name__ == '__main__':
    pytest.main(['-vs','--capture=sys'])  # pytest的启动命令





