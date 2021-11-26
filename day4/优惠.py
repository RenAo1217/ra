"""
    Frank的商城：
        1.准备商品
        2.空的购物车
        3.钱包初始化金钱
        4.最后打印购物小条
    1.业务：
        看到商品：
            商品存在
                看金钱够：
                    成功加入购物车。
                    余额减去对应价格。
                不够：
                    穷鬼，去买其他商品。
            商品不存在：
                输入错误。
            输入Q或q，退出并结算。打印小条。
    任务：尽量多的添加商品
    任务：10个辣条优惠券（0.3），20个威猛先生优惠券（0.9），免单一张优惠券，先整体打折8后在单独打折，
        在进入商城时，随机抽取优惠券，在最后结算使用改优惠券。
"""
from collections import Counter
import random
# 超市
shop = [
    # 0     1
    ["酱油", 20],  # 0
    ["醋", 15],  # 1
    ["腊肠", 50],  # 2
    ["卫龙", 5.5],
    ["电饭煲", 299],
    ["威猛先生", 60],
    ["软华子", 70],  # 抽烟
    ["鸡蛋面", 10]
]
# 购物车
mycar = []
# 初始化钱包
money = 1000
print("开始选择您的商品，您的钱包为：",money)
# 抽取优惠券
while True:
    a = input("请按1抽取您的优惠券:")
    if a == "1":
        w = random.randint(1, 31)
        if w <= 10:
            print("恭喜抽中卫龙3折券")
            b = 0.3
            break
        elif 10 < w <= 30:
            print("恭喜抽中威猛先生9折券")
            b = 0.9
            break
        else:
            print("恭喜抽中免单券")
            b = 0
            break
    else:
        print("输入错误,请重新输入")

#       枚举
while True:
    for i in enumerate(shop):  # 列举商品
        print(i)
    n = input("请选择商品")  # str  转换成int类型
    # 一个元素在某一个容器里面：
    if n.isdigit():  # .isdigit判读字符串内是不是由数字组成
        n = int(n)  # 把str转换成int
        if n < len(shop):  # 判断输入的范围
            if money > shop[n][1]:  # 钱够不够
                mycar.append(shop[n])  # 加入购物车
                if n == 3 and b == 0.3:
                    money = money - shop[n][1] * b * 0.8
                elif n == 4 and b == 0.9:
                    money = money - shop[n][1] * b * 0.8
                elif b == 0:
                    money = money
                else:
                    money = money - shop[n][1] * 0.8  # 减钱
            else:
                print("穷鬼死一边去！！！！")
        else:
            print("请输入正确的商品编号")
        print("此商品已经加入购物车，您的余额为：", money)
    elif n == "q" or n == "Q":  # 输入内容退出并打印小条
        print("再见,以下是您购买的商品",money)
        for i in enumerate(mycar):
            print(i)
        print("余额:", money)
        break
    else:
        print("您输入的有误")