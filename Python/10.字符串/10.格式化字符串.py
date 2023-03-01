CPU='Inter'
GPU='NVIDIA'
N=4090
# %()：
print('GPU:%s,型号：%d'%(GPU,N))

# .format()
print('CPU:{2};GPU:{0},型号：{1}'.format(GPU,N,CPU))

# f-string
print(f'CPU:{CPU};GPU:{GPU},型号：{N}')