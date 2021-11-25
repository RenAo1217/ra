# 求和
n=0
for i in range(0,10):
    print("请输入数字：")
    a = int(input())
    n += a
print("你的数字综合为：",n)

# 最大数
n=0
for i in range(0,10):
    print("请输入数字：")
    a = int(input())
    if a>n:
        n=a
print("你的数字最大为：",n)

# 平均数
n=0
for i in range(0,10):
    print("请输入数字：")
    a = int(input())
    n=n+a
print("你的数字平均数为：",n/10)