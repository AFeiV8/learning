keys=['NVIDIA','Inter','AMD']
values=[1,2,3]
dic={i:k for i,k in zip(keys,values)}
print(dic)

#当两列表元素个数不相同时，以数量少的为输出的键值对个数
values=[1,2,3,4]
dic={i:k for i,k in zip(keys,values)}
print(dic)