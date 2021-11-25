x=int(input("请输入一个数X:"))
y=int(input("请输入一个数Y:"))
z=int(input("请输入一个数Z:"))

if (x+y>z) and (x+z>y)and(z+y>x):
    if x==y==z:
        print("等边三角形")
    elif(x==y or x==z or y==z):
        print("等腰三角形")
    elif (x*x+y*y==z*z)or(x*x+z*z==y*y)or(z*z+y*y==x*x):
        print("直角三角形")
    else:
        print("不规则三角形")
else:
    print("不是三角形")