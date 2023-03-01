#常用的据数据类型：int,float,bool,str(被加上单、双、三引号的)

#整数类型：默认十进制,加对应符号后显示其对应进制的十进制数
print('二进制：',0b1010101)
print('八进制：',0o15763)
print('十六进制：',0x108998)

#浮点类型：浮点数相加可能会出现小数位数不确定的情况
a=1.1
b=2.2
print(a+b)  #解决方式：from decimal import Decimal
from decimal import Decimal
print(Decimal('1.1')+Decimal('2.2'))

#布尔类型：可转为整数参与运算
B1=True
B2=False
print(B1+1)
print(B2+1)

#字符串类型：当使用三引号定义时，可跨行
str='''NVIDIA
        66'''
print(str)