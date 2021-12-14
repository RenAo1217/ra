'''
    诺基亚：
        打电话：对方号码，来电铃声，归属地

        打电话：对方号码，来电铃声，归属地，提示信息，大头贴，录音
'''
import time
class  OldPhone:
    phoneNumber = ""
    voice = ""
    address = ""

    def call(self,number):
        print(self.phoneNumber,"正在给",number,"打电话。本机归属地:",self.address,"。")
        print("正在响铃：",self.voice)
        for i in range(8):
            print(".",end="")
            time.sleep(1)
        print("对方已接通!")


class NewPhone(OldPhone):
    information = ""
    picture = ""
    mic = False

    def call(self,number):
        # 老功能老代码执行
        super().call(number)

        # 新功能自己来做
        self.mic = True
        print("已经开启了录音功能！设置对方大头贴为：",self.picture,"【对方是：",self.information,"】")


phone = NewPhone()
phone.phoneNumber = "13552648187"
phone.voice = "江南style"
phone.picture = "野猪佩奇"
phone.information = "快递诈骗"
phone.address  = "北京移动"

phone.call("15556897458")










