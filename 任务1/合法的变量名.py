
while True:
    s = input('变量名:')
    #定义退出
    if s == 'exit':
        print('欢迎下次使用')
        break
    #判断字符串第一个变量是否满足条件
    if s[0].isalpha() or s[0] == '_':
        for i in s[1:]:
            #判断字符串以后的变量是否满足条件
            if not(i.isalnum() or i == '_'):
                print('%s变量名不合法' %s)
                break
        else:
            print('%s变量名合法' %s)
    else:
        print('%s变量名不合法' %s)