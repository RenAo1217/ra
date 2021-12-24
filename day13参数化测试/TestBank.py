from unittest import TestCase

import xlrd
from ddt import ddt
from ddt import data
from ddt import unpack
from 工商银行完整版 import bank_addUser

#username,password,country,province,street,door,money
# da =  [
#     ["jason","admin","cn","安徽省","桃源路","s001",5600,1],
#     ["jason", "admin", "cn", "安徽省", "桃源路", "s001", 5600, 2]
# ]
da = xlrd.read(r'C:\Users\Hasee\Desktop\python学习\python任务\day13参数化测试\计算器数据.xlsx')  # 参数化数据用文件参数化


@ddt
class TestBank(TestCase):
    @data(*da)
    @unpack
    def testAddUser(self, a, b, c, d, e, f, g, h, xlwt=None):
        s = bank_addUser(a,b,c,d,e,f,g)
        if s == h:  # 测试结果回写到excle表里
            xlwt.write(1,3,"成功！")
        else:
            xlwt.write(1,3,"失败！")
        self.assertEqual(s,h)






