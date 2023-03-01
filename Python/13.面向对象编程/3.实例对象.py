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

gpu1=GPU('RTX',4090)
print(gpu1)
print(type(gpu1))
print('-----------------')
print(gpu1.name)
print(gpu1.num)