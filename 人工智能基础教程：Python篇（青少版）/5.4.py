import collections
file = open('E:/GitHub/children-python/人工智能基础教程：Python篇（青少版）/testfile.txt')
str = file.read().split(' ')
n = collections.Counter(str)
print(n['the'])
s = zip(n.values(), n.keys())
output = open(
    'E:/GitHub/children-python/人工智能基础教程：Python篇（青少版）/testresult.txt', 'w')
for item in sorted(s, reverse=True):
    output.write("{0}{1}\n".format(item[1], item[0]))
