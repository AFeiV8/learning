#赋值运算符：连续赋值，id改变
print('--------赋值运算符--------')
a=20
print(a,id(a))
a+=30
print(a,id(a))
a-=10
print(a,id(a))
a*=2
print(a,id(a))
a/=3
print(a,id(a))
a//=2
print(a,id(a))
a%=3
print(a,id(a))

a,b,c=10,20,30  #解包赋值
print(a,b,c)
c,b,a=a,b,c     #变量之间交换value
print(a,b,c)