shop={"昌平":{"麻辣烫店":"麻辣烫","跑腿费":2,"客户地址":"101室"}}#1
shop1={"房山":{"麻辣烫店":"麻辣烫","跑腿费":3,"客户地址":"102室"}}#2
client={"昌平":{"翻斗花园":"101室"}}#1
client1={"房山":{"流星花园":"102室"}}#2
money=0
import random
while True:
    sj = random.randint(1,2)
    if sj != 2:
        print("商家为昌平麻辣烫店")
        money = money + 2
        break
    else:
        print("商家为房山麻辣烫")
        money = money + 3
        break
print("骑手已接单")
while True:
    mj = random.randint(1,2)
    if mj != 2:
        print("买家为昌平101室")
        money = money + 2
        print("骑手已送达，请楼下取餐")
        break
    else:
        print("买家为房山102室")
        money = money + 3
        print("骑手已送达，请楼下取餐")
        break
print("您的外卖请收好，小票金额为", money)