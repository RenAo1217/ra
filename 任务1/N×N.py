#使用while循环实现NxN乘法表的打印。
i=1
while i<=9:
    j=1
    while j<=i:
        print("%dx%d=%d"%(i,j,i*j),end='  ')
        j=j+1
    print('   ')
    i+=1