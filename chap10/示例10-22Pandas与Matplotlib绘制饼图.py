import pandas as pd
import matplotlib.pyplot as plt
from math import sqrt

# 读取Excel文件
df = pd.read_excel('train_data.xlsx')
print(df)

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.figure(figsize = (10,6))
# figure(figsize = (10,6))
labels = df['ID']
y = df['WAAC']
print(type(df))
print(labels)
print(y)

plt.pie(y, labels = labels, autopct = '%1.1f%%', startangle = -90)

plt.axis('equal')
plt.title('WAAC与ID关系')
plt.show()

print(sqrt(5))
