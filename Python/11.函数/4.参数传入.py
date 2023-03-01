#当输入参数为列表形式时可用*lst传入
#当输入参数为字典形式时可用**dict传入
def fun1(*args):
    print(args)

def fun2(**args):
    print(args)

lst=[10,20,54,65,95,75,56]
dict={'a':542,'b':256,'c':425}
fun1(*lst)
fun2(**dict)

def fun3(a,b,*,c,d):  #重*之后只能采用关键字实参传递
    print(a,b,c,d)
fun3(10,20,c=30,d=40)