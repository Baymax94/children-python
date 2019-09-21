from urllib import request
from bs4 import BeautifulSoup

url = "http://www.jianshu.com"
headers = {
    'User-Agent': 'Mozilla/5.0(Windows NT 10.0;Win64;x64)AppleWebKit/537.36(KHTML,like Gecko)Chrome/55.0.2883.87Safari/537.36'}
page = request.Request(url, headers=headers)
page_info = request.urlopen(page).read().decode('utf-8')
soup = BeautifulSoup(page_info, 'html.parser')
titles = soup.find_all('a', 'title')
file = open(
    "E:/GitHub/children-python/人工智能基础教程：Python篇（青少版）/testwebinfo.txt", "w")
for title in titles:
    file.write(title.string+'\n')
    file.write("http://www.jianshu.com"+title.get('href')+'\n\n')
# 读取web页面信息
