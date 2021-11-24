import random
mht=random.randint(0,10)
money =5000
i=0
print(mht)
while i<15:
    num=input("请输入您猜的数字")
    num=int(num)
    if num<mht:
        money-=100
        print("小了，您的金币还剩",money)
    elif num>mht:
        money-=100
        print("大了，您的金币还剩",money)
    else:
        money+=300
        print("恭喜您猜中了，您的金币还剩",money)
        break
    i=i+1