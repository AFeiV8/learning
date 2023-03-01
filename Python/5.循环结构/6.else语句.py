#当else与while或for配套使用时，只有循环体中的break未被执行时，才执行else语句的内容

a=0
while a<3:
    p=input('请输入密码：')
    if p=='8888':
        print('密码正确！')
    else:
        a+=1
        print('请重新输入！')
else:
    print('您已输入出错三次！')