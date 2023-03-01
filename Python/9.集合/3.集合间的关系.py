'''
==,!=:
A.issubset(B):A是否是B的子集
A.isuperset(B):A是否是B的超集
A.isdisjoint(B):两集合有无交集,没有交集为True，有交集为False
'''

s={10,20,30,40,50,60}
s1={10,20,30,40}
s2={10,20,90}

print(s.issubset(s1))
print(s1.issubset(s))
print(s.issuperset(s1))
print(s1.isdisjoint(s2))