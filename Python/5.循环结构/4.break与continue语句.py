#break退出循环；continue退出当次循环，进入下一次循环
#当存在多层循环时，break和continue用于控制本层循环
s=0
for i in range(1,101):
    if i%2!=0:
        continue
    else:
        s+=i
print(s)

for _ in  range(3):
    for i in range(1,11):
        if i%2==0:
            break
        print(i)

for _ in range(3):
    for i in range(1,11):
        if i%2==0:
            continue
        print(i,end='\t')
    print()