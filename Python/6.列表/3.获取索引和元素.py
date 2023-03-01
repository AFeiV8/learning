#存在相同元素时，只能拿到该元素第一次出现的索引；列表中无想查询的元素时：ValueError
lst=['NVIDIA','GPU','RTX',4090]
print(lst.index('GPU'))
print(lst.index(4090,0,4))

#按照索引获取元素时,正方向：0～N-1；负方向：-1～-N
#指定索引不存在时：IndexError
print(lst[-3])