# 除去列表中的重复项
list=['a','b','c','t','u','q','c','p','e','b','c','a','u']
re_list=[]

for i in list:
    if not i in re_list:
        re_list.append(i)

print(re_list)