'''
__init__():对象初始化
__len__()：重写可实现输出实例对象的实例属性的长度的功能
__add__()：重写可实现实例对象间的相加操作
__new__()：用于创建对象
'''

class GPU:
    def __init__(self,name,num):
        self.name=name
        self.num=num
    def __add__(self,other):
        print(self.name+other.name)
    def __len__(self):
        return (len(self.name))

gpu1=GPU('RTX',4090)
gpu2=GPU('GTX',1060)
gpu1+gpu2
print(len(gpu1))