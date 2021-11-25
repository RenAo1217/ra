#python内置方法

print("请输入两个整数：")
a = int(input("第一个整数："))
b = int(input("第二个整数："))
a,b = b,a
print("使用Python内置方法得出结果：")
print("a变换后为：%d"% a)
print("b变换后为：%d"% b)