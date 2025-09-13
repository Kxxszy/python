import matplotlib.pyplot as plt
from matplotlib import font_manager

# 设置中文字体（macOS 自带的苹方）
plt.rcParams['font.sans-serif'] = ['PingFang SC']  # 或者 'Heiti TC', 'STHeiti'
plt.rcParams['axes.unicode_minus'] = False  # 让负号正常显示

plt.title("中文标题测试")
plt.plot([1, 2, 3], [4, 5, 6])
plt.show()