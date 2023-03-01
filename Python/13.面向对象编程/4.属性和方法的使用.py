class GPU:
    company='NVIDIA'
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

gpu1=GPU('RTX',4090)
gpu2=GPU('GTX',1060)
#类属性：
print(gpu1.company)
print(gpu2.company)
#实例属性：
print(gpu1.name,gpu1.num)
print(gpu2.name,gpu2.num)
#实例方法
gpu1.m()
GPU.m(gpu1)
#静态方法：
gpu1.sm()
GPU.sm()
#类方法：
gpu1.cm()
GPU.cm()