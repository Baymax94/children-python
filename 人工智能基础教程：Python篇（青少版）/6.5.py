import matplotlib.pyplot as plt
Score = [95, 89, 65, 90]
Subject = ['Math', 'Chinese', 'English', 'Synthetical']
cols = ['c', 'm', 'r', 'b']

plt.pie(
    Score,
    labels=Subject,
    colors=cols,
    startangle=90,
    shadow=False,
    explode=(0.1, 0, 0, 0),
    autopct='%1.1f%%')
plt.title("test Graph")
plt.show()

# 饼图
