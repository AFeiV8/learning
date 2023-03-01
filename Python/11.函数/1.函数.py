'''
参数传递：位置实参，关键字实参
在函数调用过程中，不会改变不可变对象的实参的值，会改变可变对象的实参的值
当函数返回值为多个的时候，返回的是元组
'''

def fun(lst):
    dan=[]
    shuang=[]
    for i in lst:
        if i%2:
            dan.append(i)
        else:
            shuang.append(i)
    return dan,shuang

a=[1,5,6,4,20,31,65,45,25,99,88,44,75]
result=fun(a)
print(result)

