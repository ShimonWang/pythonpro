import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']  # class matplotlib.RcParams(*args, **kwargs):
# 用于配置参数的字典样式的键值存储，包括验证  font.sans-serif:字体.无衬线字体
x = [1,2,3,4,5]
y = [2,5,8,12,18]
fig,ax = plt.subplots(nrows=1, ncols=2, sharey=True)
ax1 = ax[0]
ax1.plot(x,y)
ax1.set_title("折线图")
ax2 = ax[1]
ax2.scatter(x,y, color='red')
ax2.set_title("散点图")
plt.show()