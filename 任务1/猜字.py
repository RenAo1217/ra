#继续完成上午的猜数字游戏的需求功能。
#1.    添加计数打印功能
#2.    添加次数金币功能和锁定系统功能。
import random
print("猜字游戏")
q=1000
w=0
e=0
s=random.randint(0,10)
while True:
    a=int(input("请输入一个数字"))
    if a == s:
        w += 1
        q -= 100
        print("正确")
        break
    elif a>s:
        w+=1
        q -= 100
        print("你输入的过大，金额还剩",q,"已猜次数",w)
        if q==e:
            print("金额不足，系统锁定")
            break
    elif a<s:
        w+=1
        q-=100
        print("你输入的过小，金额还剩",q,"已猜次数",w)
        if q ==e:
            print("金额不足，系统锁定")
            break
print("金额还剩",q,"已猜次数",w)