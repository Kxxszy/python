import numpy as np

# 示例：求解方程组
# 2x + y = 5
# x - 3y = -1
A = np.array([[2, 1],
              [1, -3]])
b = np.array([5, -1])

# 求解 Ax = b
x = np.linalg.solve(A, b)
print("线性方程组解:")
print(f"x = {x[0]:.2f}, y = {x[1]:.2f}")

# 验证解
print("\n验证:")
print(f"A × x = {A @ x}")
print(f"b = {b}")

# 同时求解多个方程组
# 方程组1: 2x + y = 5, x - 3y = -1
# 方程组2: x + 2y = 8, 3x - y = 1
A = np.array([[2, 1],
              [1, -3]])
B = np.array([[5, 8],
              [-1, 1]]).T  # 注意转置

x = np.linalg.solve(A, B)
print("\n多组方程解:")
print(x)