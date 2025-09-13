import matplotlib.pyplot as plt

x = [1, 2, 3, 4]

# 第一张子图
plt.subplot(2, 1, 1)       # 两行一列的第1个
plt.plot(x, [i**2 for i in x], 'r')

# 第二张子图
plt.subplot(2, 1, 2)       # 两行一列的第2个
plt.plot(x, [i**3 for i in x], 'g')

plt.show()