import requests
print("访问baidu网站 获取Response对象")
r = requests.get("https://www.baidu.com/")
print(r.status_code)
print(r.encoding)
print(r.apparent_encoding)
print("将对象编码转换成UTF-8编码并打印出来")
r.encoding = 'utf-8'
print(r.text)
