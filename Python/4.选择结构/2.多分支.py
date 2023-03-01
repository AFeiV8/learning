s=float(input('请输入学生成绩：'))
if s>=90 and s<=100:
    print('A')
elif  80<=s<=89:
    print('B')
elif s>=70 and s<=79:
    print('C')
elif s>=60 and s<=69:
    print('D')
elif s>0 and s<=59:
    print('不及格')
else:
    print('输入错误！')