import numpy as np
import matplotlib.pyplot as plt

# 模拟方向数据（0°, 45°, 90°, 135°, 180°）
directions = np.array([0, 45, 90, 135, 180])  # 单位：度
magnitudes = np.array([1, 1, 1, 1, 1])  # 统一长度

# 角度转弧度
radians = np.deg2rad(directions)

# 箭头的坐标变化
u = magnitudes * np.cos(radians)  # x 分量
v = magnitudes * np.sin(radians)  # y 分量

# 创建画布
fig, ax = plt.subplots()
ax.quiver(
    np.zeros(len(u)),  # 箭头起点 x
    np.zeros(len(v)),  # 箭头起点 y
    u,                 # 箭头 x 方向分量
    v,                 # 箭头 y 方向分量
    angles='xy', scale_units='xy', scale=1, color='blue'
)

# 坐标系设置
ax.set_xlim(-1.5, 1.5)
ax.set_ylim(-1.5, 1.5)
ax.set_aspect('equal')
ax.set_title("the effect of different directions")
plt.grid(True)
plt.show()