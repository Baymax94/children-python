words = input('请输入一个英文句子:')
d = {}
for letter in words:
    letter = letter.lower()
    if letter.isalpha():
        d[letter] = d.get(letter, 0) + 1

letters = sorted(d.keys())
for letter in letters:
    print(letter, d[letter])
