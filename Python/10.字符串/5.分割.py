'''
split(sep,maxsplit):左侧开始；sep:指定分割符号（默认为空格）；maxsplit：最大分割次数
rsplit(sep,maxsplit):右侧开始；sep:指定分割符号（默认为空格）；maxsplit：最大分割次数
都将得到列表
'''

s='NVIDIA GPU RTX 4090'
S1='NVIDIA|GPU|RTX|4090'
lst1=s.split()
lst2=s.split(maxsplit=2)
lst3=s.split(sep='|')
print(lst1)
print(lst2)
print(lst3)
