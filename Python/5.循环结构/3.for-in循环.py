# for 自定义变量 in 遍历对象:
#如果不需要自定义变量，用_代替
for _ in range(6):
    print('NVDIA RTX4090')

s=0
for i in range(1,101):
    if i%2==0:
        s+=i
print(s)