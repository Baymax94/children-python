'''
程序：百分制成绩转换为等级制
作者：苏秦@小海豚科学馆公众号
来源：图书《Python趣味编程：从入门到人工智能》
'''
score = int(input('请输入成绩：'))
if score < 60:
    print('不合格')
elif 60 <= score <= 69:
    print('合格')
elif 70 <= score <= 89:
    print('良好')
elif 90 <= score <= 100:
    print('优秀')
else:
    print('错误数据')
