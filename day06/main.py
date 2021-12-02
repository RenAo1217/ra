# from random import randint
import random
print("=====================")
print("|  ===中国工商银行=== |")
print("=====================")
print("|1、开户             |")
print("|2、存钱             |")
print("|3、取钱             |")
print("|4、转账             |")
print("|5、查询             |")
print("=====================")
#定义一个空字典,当作数据库
bank={}
#bank={'Frank': {'account': 29073386, 'password': '123456', 'country': '中国', 'province': '山东', 'street': '1大街', 'door': '001', 'bank_name': '中国工商银行', 'money': 0}
bank_name="中国工商银行"
#定义方法————用来添加用户的
def useradd():
    account=random.randint(10000000,99999999)
    username=input("请输入您的姓名")
    password=input("请输入您的密码")#如果定义为str   ”“
    country=input("\t\t请输入您的国家")#\t表示一个tab
    province=input("\t\t请输入您的省份")
    street=input("\t\t请输入您的街道")
    door=input("\t\t请输入您的门牌号")
    gift=bankadd(account,username,password,country,province,street,door)#位置对应
    if gift =="1" :
        print("开户成功,一下是您的详细信息")
        #模板
        info='''
                --------工商银行-------
                    1、账号：%s
                    2、姓名：%s
                    3、密码：******
                    4、国家：%s
                    5、省份：%s
                    6、街道：%s
                    7、门牌：%s
                    8、余额：%s
        '''
        print(info % (account,username,country,province,street,door,bank[username]["money"]))
    elif gift =="2":
        print("请使用其他用户")
    elif gift =="3":
        print("数据库已满")

#往字典里面存数据
def bankadd(account,username,password,country,province,street,door):
    if username in bank:#  姓名在不在bank的键里
        return "2"
    elif len(bank)>=100:
        return "3"
    bank[username]={
        "account":account,#从useradd的account获取的随机数
        "password":password,
        "country":country,
        "province":province,
        "street":street,
        "door":door,
        "bank_name":bank_name,
        "money":0
    }
    return "1"
while True:
    box=input("请输入编号")
    if box=="1":
        print("1、开户")
        useradd()
    elif box =="2":
        print("2、存钱")