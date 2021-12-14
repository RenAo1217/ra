class oldphone():
    pinpai=""
    def setpinpai(self,pp):
        self.pinpai=pp
    def getpinpai(self):
        return self.pinpai
    def show(self,name):
        print("正在使用",self.pinpai,"牌的手机给",name,"打电话")
o=oldphone()
o.setpinpai("华为")
o.show("阿飞")
class new(oldphone):
    def show(self,name):
        print("语音拨号中..")
        super().show(name)
        print("品牌为",self.pinpai,"的手机很好用")
o=new()
o.setpinpai("vivo")
o.show("小阿飞")



class chushi():
    name=""
    age=0
    def setname(self,n):
        self.name=n
    def getname(self):
        return self.name
    def  setage(self,a):
        self.age=a
    def getage(self):
        return  self.age
    def fan(self):
        print(self.name,"蒸饭")
class cai(chushi):
    def chao(self):
        print(self.name,"烧菜")
class sun(cai):
    def a(self):
        print(self.name,self.age)
c=sun()
c.setname("阿飞")
c.setage(5)
c.a()



class people():
    name=""
    age=0
    sex=""
    def setname(self,n):
        if n =="":
            print("必须填，不能为空")
        else:self.name=n
    def getname(self):
        return self.name
    def setage(self,a):
        if a ==0:
            print("不能为0")
        else:self.age=a
    def getage(self):
        return self.age
    def setsex(self,s):
        if s =="男"or s=="女":
            self.sex=s
        else:print("别瞎填！！！")
    def getsex(self):
        return self.sex
class huo(people):
    def ganhuo(self):
        print("姓名：",self.name,"年龄：",self.age,"性别:",self.sex,"挖煤")
a=huo()
a.setname("啊小飞")
a.setsex("男")
a.setage(25)
a.ganhuo()
class student(people):
    def lenren(self):
        print("姓名：",self.name,"年龄：",self.age,"性别:",self.sex,"玩游戏")

    def sing(self):
        print("姓名：", self.name, "年龄：", self.age, "性别:", self.sex, "跳舞")
a=student()
a.setname("阿飞飞")
a.setsex("女")
a.setage(18)
a.lenren()
a.sing()