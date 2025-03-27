import matplotlib.pyplot as plt


x = [1, 2, 3, 4, 5]
y = [10, 20, 30, 40, 50]
fig = plt.figure()
ax1 = fig.add_subplot(111)
ax1.plot(x,y)
ax2 = ax1.twiny()
plt.show()