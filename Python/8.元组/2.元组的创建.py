'''当不使用内值函数创建时且元组只含有一个元素时，
需要使用逗号和小括号，不加逗号则是其本身的数据类型
'''

t=('NVIDIA','Inter','AMD')
print(t)
t1=('NVIDIA',)
print(type(t1))
t2=tuple(('NVIDIA','Inter','AMD'))
print(t2)