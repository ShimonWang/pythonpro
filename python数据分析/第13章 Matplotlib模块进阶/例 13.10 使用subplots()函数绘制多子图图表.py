import matplotlib.pyplot as plt


figure,axes = plt.subplots(2,2)
axes[0,0].plot([1,2,3,4,5])
axes[0,1].plot([1,2,3,4,5], [2,5,8,12,18], 'ro')
x = [1,2,3,4,5,6]
height = [10,20,30,40,50,60]
axes[1,0].bar(x, height)
x = [2,5,12,70,2,9]
axes[1,1].pie(x, autopct='%1.1f%%')
plt.show()