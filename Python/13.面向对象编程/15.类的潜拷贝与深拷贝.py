'''
浅拷贝：一般都是浅拷贝，对象包含的作为实例参数的子对象内容不拷贝，
        因此源对象与拷贝对象会引用同一个子对象
深拷贝：使用copy模块的deepcopy函数，递归拷贝对象中包含的子对象，
        源对象和拷贝对象所有的子对象不相同,
        对象包含的作为实例参数的子对象有了新的实例
'''
import copy
class CPU:
    pass
class GPU:
    pass
class PC():
    def __init__(self,cpu,gpu):
        self.cpu=cpu
        self.gpu=gpu

#浅拷贝：
cpu=CPU()
gpu=GPU()
pc1=PC(cpu,gpu)
pc2=copy.copy(pc1)
print(pc1 is pc2)
print(pc1.cpu is pc2.cpu)
print(pc1.gpu is pc2.gpu)

#深拷贝：
print('---------------')
pc3=copy.deepcopy(pc1)
print(pc1 is pc3)
print(pc1.cpu is pc3.cpu)
print(pc1.gpu is pc3.gpu)