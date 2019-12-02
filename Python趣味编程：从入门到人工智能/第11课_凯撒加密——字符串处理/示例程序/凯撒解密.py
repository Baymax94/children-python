'''
程序：凯撒解密
作者：苏秦@小海豚科学馆公众号
来源：图书《Python趣味编程：从入门到人工智能》
问题：编写凯撒密码的解密程序，将密文“Krz duh brx grlqj”还原成明文。
'''
#输入明文
text = input('请输入密文:')

#凯撒解密
s = ''
i = 0
while i < len(text):
    c = text[i]
    if 'd' <= c <= 'z' or 'D' <= c <= 'Z':
        c = chr(ord(c) - 3)
    elif 'a' <= c <= 'c' or 'A' <= c <= 'C':
        c = chr(ord(c) + 23)
    s = s + c
    i = i + 1
    
#输出明文   
print('输出明文:' + s)
