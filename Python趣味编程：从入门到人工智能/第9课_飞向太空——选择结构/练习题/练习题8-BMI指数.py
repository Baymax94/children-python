'''
程序：计算BMI指数
作者：苏秦@小海豚科学馆公众号
来源：图书《Python趣味编程：从入门到人工智能》
'''
mass = float(input('请输入体重(kg)：'))
height = float(input('请输入身高(m)：'))

bmi = round(mass / height / height)
if bmi < 18.5 :
    body = '偏瘦'
elif 18.5 <= bmi < 24 :
    body = '正常'
elif 24 <= bmi < 28 :
    body = '超重'
elif bmi >= 28 :
    body = '肥胖'

print(body)
