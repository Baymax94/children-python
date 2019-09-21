import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data = pd.DataFrame(np.random.randn(1000, 2), columns=list("AB"))
print(data.head())
data.plot.scatter(x='A', y='B')

plt.text(2, 2, 'Simple A')
plt.annotate('boundary', xy=(-3, -2), xytext=(-2.5, -2.5),
             arrowprops=dict(facecolor='red'))
plt.grid(True)
plt.show()

# 图像注释
