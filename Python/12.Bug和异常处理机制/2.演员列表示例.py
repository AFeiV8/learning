lst=[{'title':'肖生克的救赎','type':['犯罪','剧情'],'actors':['T','M']},
     {'title':'霸王别姬','type':['爱情','剧情'],'actors':['Z','G']},
     {'title': '控方证人', 'type': ['犯罪', '剧情'], 'actors': ['B', 'A']}
     ]

while 1:
    n = input('请输入演员姓名：')
    for i in lst:
        actors_lst=i['actors']
        for j in actors_lst:
            if n in j:
                print(n,'出演了',i['type'],'题材的电影：',i['title'])