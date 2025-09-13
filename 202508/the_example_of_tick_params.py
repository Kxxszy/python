import matplotlib.pyplot as plt

plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()

ax.plot([0, 1], [0, 1])

# 设置X轴刻度
ax.tick_params(axis='x',           # 只设置X轴
               direction='inout',  # 刻度线向内外延伸
               length=8,           # 刻度线长度
               width=2,            # 刻度线宽度
               colors='red',       # 刻度线和标签颜色
               labelsize=14)       # 标签字体大小

# 只隐藏Y轴的标签
ax.tick_params(axis='y', labelleft=False)

plt.show()