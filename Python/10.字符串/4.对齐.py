'''
center(w,symbol):居中对齐，symbol默认为空格，w小于字符长度时显示原字符串
ljust(w,symbol):左对齐，symbol默认为空格，w小于字符长度时显示原字符串
rjust(w,symbol):右对齐，symbol默认为空格，w小于字符长度时显示原字符串
zfill(w)：右对齐，左侧用零填充
'''
s='NVIDIA'
a='-618'
s1=s.center(8,'*')
s2=s.rjust(8,'*')
s3=a.zfill(6)
print(s1)
print(s2)
print(s3)