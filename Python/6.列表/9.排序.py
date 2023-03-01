'''
sort():默认升序排序，可指定reverse=True进行降序排列
sorted():默认升序排序，可指定reverse=True进行降序排列，将产生新的列表对象

'''

lst=[20,40,10,98,54]
print(lst)
lst.sort(reverse=True)
print(lst)
lst=[20,20,10,98,54]

lst1=sorted(lst)
lst2=sorted(lst,reverse=True)
print(lst1)
print(lst2)