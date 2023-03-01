'''
查询：
index():找第一次出现，不存在抛ValueError
rindex():找最后一次出现，不存在抛ValueError
find():找第一次出现，不存在返回-1
rfind():找最后一次出现，不存在返回-1
'''

a='NVIDIA'
print(a.index('D'))
print(a.rindex('I'))
print(a.find('c'))