# *:个数可变的位置参数，返回值为元组
def fun1(*args):
    print(args)

# **:个数可变的关键字参数，返回值为字典
def fun2(**args):
    print(args)

#两总参数都存在时，*在前，**在后,位返元关返典
def fun3(*args1,**args2):
    print(args1,args2)

fun1(10,50,640,85,64)
fun2(a=10,b=50,c=60)
fun3(10,20,50,46,15,a=54,b=95,c=65)