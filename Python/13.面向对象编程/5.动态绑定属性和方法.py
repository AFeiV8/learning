class GPU:
    def __init__(self,name,num):
        self.name=name
        self.num=num
    def m(self):
        print(self.name,self.num)
#绑定属性：
gpu1=GPU('RTX',4090)
gpu1.company='NVIDIA'
print(gpu1.company)
#绑定方法：
def show():
    print('动态绑定方法')
gpu1.show=show
gpu1.show()