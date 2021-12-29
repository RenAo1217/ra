import unittest
from HTMLTestRunner import HTMLTestRunner # 测试运行器，就能生成测试报告

# 1.加载5条用例

tests = unittest.defaultTestLoader.discover(r"C:\Users\Hasee\Desktop\python学习\python任务\day17\汉科软自动化",pattern="LonginTEST.py")

# 2.创建运行器
runner = HTMLTestRunner.HTMLTestRunner(
    title = "这是计算机的测试报告",
    description="自动化修改头像测试报告",
    verbosity=1,
    stream = open(file="计算器.html",mode="w+",encoding="utf-8")
)

# 3.运行
runner.run(tests)