'''
执行过程：
当执行实例化任务时，先将类传给new中cls，对象创建完成后，将对象传给init中的self，初始化完毕之后传给实例对象名
'''
class GPU(object):
    def __new__(cls, *args, **kwargs):
        print('cls的id：{0}'.format(id(cls)),'此时正在进行实例化的new中cls的传入')
        gpu=super().__new__(cls)
        print('gpu的id：{0}'.format(id(gpu)), '此时正在进行实例化的new过程，已经产生了对象gpu')
        return gpu
    def __init__(self,name,num):
        print('self的id：{0}'.format(id(self)),'此时正在进行实例化的init过程，传入self')
        self.name=name
        self.num=num

print('GPU的id：{0}'.format(id(GPU)),'类对象')
gpu1=GPU('RTX',4090)
print('gpu1的id：{}'.format(id(gpu1)))

