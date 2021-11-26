'''
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
'''
#超市
import random
shop=[
    ["酱油",20],#0
    ["醋",15],#1
    ["腊肠",50],#2
    ["卫龙",5.5],
    ["电饭煲",299],
    ["威猛先生",60],
    ["软华子",70],
    ["鸡蛋面",10]
]
num1=random.randint(2,2)
print("恭喜获取%d张优惠卷"%num1)
num2=random.randint(3,3)
print("这张优惠卷为%d折"%num2)
num3=random.randint(0,8)
num4=shop[num2][0]
print("获取的优惠券为辣条卷%d折"%num2)
num5=random.randint(7,7)
print("这张优惠卷为%d折"%num5)
num6=shop[num2][0]
print("获取的优惠券为威猛先生卷%d折"%num5)
num7=random.randint(8,8)
print("新开业每样商品优惠卷为%d折"%num7)
#购物车
mycar=[]
#初始化钱包
money=1000
print("开始选择您的商品，您的钱包为：",money)
#       枚举
while True:
    for i in enumerate(shop):#列举商品
        print(i)
    o=input("请选择商品")#str  转换成int类型
    # 一个元素在某一个容器里面：
    if o.isdigit():#.isdigit判读字符串内是不是由数字组成
        o=int(o)#把str转换成int
        if o <len(shop):#判断输入的范围
            if money>shop[o][1]:#钱够不够
                mycar.append(shop[o])#加入购物车
                money=money-shop[o][1]*0.8#减钱
                print("此商品已经加入购物车，您的余额为：",money)
            else:print("穷鬼，死一边去")
        else:print("请输入正确的商品编号")
    elif o =="q" or o=="Q":#输入内容退出并打印小条
        print("再见,以下是您购买的商品，剩余价格为：",money)
        for i in enumerate(mycar):
            print(i)
        break
    else:print("您输入的有误")
