'''
remove():一次只删除一个元素；重复的元素只删除一个；元素不存在报ValueError
pop():删除指定索引位置上的元素；不指定删最后一个；索引不存在报IndexError
切片：删除多个元素
clear():清空列表
del:删除列表
'''

#产生新对象的切片和不产生新对象的切片
lst=['NVIDIA',4090,'RTX','GPU',618,888]
lst1=lst[1:3]
lst[1:3]=[]
print(lst1)
print(lst)

lst.clear()
print(lst)

#del lst