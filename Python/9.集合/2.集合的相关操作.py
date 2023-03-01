'''
增：add()：添加一个;update()：添加多个,当添加字符串有重复字符时，只添加一个,不能添加数字
删：remove()：删除一个指定元素，抛KeyError;  discard()：删除一个指定元素，不抛异常;
    pop()：删除一个任意元素;clear()：清空集合
'''

s={'NVIDIA','Inter','AMD'}
s.add(55)
print(s)
s.update('666','888','666')
print(s)
s.remove('6')
print(s)
s.pop()
print(s)
