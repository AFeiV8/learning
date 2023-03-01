class PC:
    def __init__(self,sym,n):
        self.sym=sym
        self.n=n
    def m(self):
        print(self.sym,self.n)

class GPU(PC):
    def __init__(self,sym,n,type,num):
        super().__init__(sym,n)
        self.type=type
        self.num=num

gpu1=GPU('Linux',5.13,'RTX',4090)
gpu1.m()