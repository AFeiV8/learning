'''
同一个实例赋值给了不同变量,如果创建了不同的实例id一定不一样
'''
class GPU():
    pass
gpu1=GPU()
gpu2=gpu1
print(gpu1 is gpu2)
