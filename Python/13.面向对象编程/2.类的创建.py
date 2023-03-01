'''
类的组成：
    类属性：类中方法外的变量，被该类的所有实例对象所共享
    实例属性：实例对象将传入的参数
    实例方法：def m(self):  必须通过至少传入一个参数的实例对象才能被调用，传入的是对象
    静态方法：@staticmethod
            def sm():     必须传入一个参数，可通过类名调用也可通过实例调用
    类方法：@classmethod
            def cm(cls):  参数可为空，可通过类名调用也可通过实例调用，传入的是类
'''
class GPU:
    conpany='NVIDIA'
    def __init__(self,name,num):
        self.name=name
        self.num=num
    def m(self):
        print(self.name,self.num)
    @staticmethod
    def sm():
        print('静态方法')
    @classmethod
    def cm(cls):
        print('类方法')

print(GPU)
print(type(GPU))
