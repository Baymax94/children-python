import json
with open('E:/GitHub/children-python/人工智能基础教程：Python篇（青少版）/test_package.json') as file:
    data = json.load(file)

print(data["name"])
print(data["result"][0]["citynm"], data["result"]
      [0]["days"], data["result"][0]["tempture"])
print(data["result"][1]["citynm"], data["result"]
      [1]["days"], data["result"][1]["tempture"])

# 读取json文件
