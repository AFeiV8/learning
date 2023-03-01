'''
集合相当于字典的key，序列由hash函数决定，元素不允许重复
'''

s={1,2,3,4}
print(s)
a=list(s)[2]
print(type(a))
s1=set(range(1,5))
print(s1)

s2=set('NVIDIA')
print(s2)

print(hash('V') > hash('N'))