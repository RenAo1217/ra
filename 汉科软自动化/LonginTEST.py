from selenium import webdriver
import unittest
from unittest import TestCase
from selenium import webdriver
from pywinauto.keyboard import send_keys
import time


class TestHKr(TestCase):

    def testlogin1(self):
        # 准备成功数据
        username = "root"
        password = "root"
        expect = "Student Login"  # 期望结果

        # 执行测试
        driver = webdriver.Chrome()
        driver.get("http://localhost:8080/HKR")
        driver.maximize_window()
        driver.find_element_by_xpath("//*[@id='loginname']").send_keys(username)
        driver.find_element_by_xpath("//*[@id='password']").send_keys(password)
        driver.find_element_by_xpath("//*[@id='submit']").click()
        driver.find_element_by_xpath("//*[@id='img']").click()
        f = driver.find_element_by_xpath("//*[@id='lablefile']")
        f.click()
        time.sleep(2)
        send_keys(r"D:\game.jpg")
        send_keys("{VK_RETURN}")
        time.sleep(2)
        driver.find_element_by_xpath("/html/body/div[4]/div[2]/div[2]/div[2]/div/div[4]/button").click()

        # 获取浏览器标题信息
        result = driver.title
        if result != expect:
            driver.save_screenshot("错误.jpg")
        driver.quit()
        # 断言
        self.assertEqual(result, expect)

    def testlogin2(self):
        # 准备成功数据
        username = "root"
        password = "root"
        expect = "账户名错误或密码错误!别瞎弄!"  # 期望结果,id='msg_uname'

        # 执行测试
        driver = webdriver.Chrome()
        driver.get("http://localhost:8080/HKR")
        driver.maximize_window()
        driver.find_element_by_xpath("//*[@id='loginname']").send_keys(username)
        driver.find_element_by_xpath("//*[@id='password']").send_keys(password)
        driver.find_element_by_xpath("//*[@id='submit']").click()

        # 获取实际错误信息
        result = driver.find_element_by_xpath("/html/body/div[7]/div[2]/div[2]").text
        if result != expect:
            driver.save_screenshot("错误.jpg")
        driver.quit()
        # 断言
        self.assertEqual(result, expect)


    def testlogin3(self):
        # 准备成功数据
        username = "root"
        password = "root"
        expect = "tt"  # 期望结果

        # 执行测试
        driver = webdriver.Chrome()
        driver.get("http://localhost:8080/HKR")
        driver.maximize_window()
        driver.find_element_by_xpath("//*[@id='loginname']").send_keys(username)
        driver.find_element_by_xpath("//*[@id='password']").send_keys(password)
        driver.find_element_by_xpath("//*[@id='submit']").click()
        driver.find_element_by_xpath("//*[@id='_easyui_tree_10']/span[4]/a").click()
        time.sleep(3)

        # 获取实际错误信息
        result = "tt"
        if result != expect:
            driver.save_screenshot("错误.jpg")
        driver.quit()
        # 断言
        self.assertEqual(result, expect)











































