import os
import allure
import pytest


pytest.main([
        "-s", "-v",
        "--capture=sys",
        "Test_framework.py",
        "--clean-alluredir",
        "--alluredir=allure-results"  # 指定结果目录
    ])

# 生成并打开 Allure 报告
os.system("allure generate allure-results -o report --clean")  # 生成报告到 report 目录
os.system("allure open ./report")