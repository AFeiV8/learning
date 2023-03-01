'''
递归的组成部分：递归的调用和递归的终止条件
'''

def fun(n):
    if n==1:
        return 1
    else:
        res=n*fun(n-1)
        return res
n=fun(5)
print(n)

def fib(i):
    if i==1:
        return 1
    if i==2:
        return 1
    else:
        return fib(i-1)+fib(i-2)

f=fib(6)
print(f)
lst=[fib(i) for i in range(1,7)]
print(lst)