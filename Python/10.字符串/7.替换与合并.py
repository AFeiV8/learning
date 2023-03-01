'''
replace(被替换对象，替换对象，替换次数):得到字符串，不影响原字符串
join():'symbol'.join(lst/str)，得到一个str
'''

str='NVIDIA GPU RTX 3080/3080'
str1=str.replace('3080','4090',1)
print(str1)

lst=['NVIDIA','GPU','RTX','3080']
str2='*'.join(lst)
print(str2)
