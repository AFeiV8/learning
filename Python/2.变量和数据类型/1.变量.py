#变量的组成：Id，type，value
#变量被多次赋值后会指向新的内存空间
a='NVIIDA'
print(id(a))
a='Intel'
print(id(a))
