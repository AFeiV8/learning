'''
intersection():交集，&
union():并集，|
difference():差集，-，A-B=A-AB
symmetric_difference():对称差集，^,A+B-AB,
集合元素不重复
'''

s={10,20,30,40,90}
s1={50,60,70,90}
s2={10,20,30,50,80,90}

print(s2.intersection(s))
print(s.union(s1))
print(s2.difference(s))
print(s2.symmetric_difference(s))