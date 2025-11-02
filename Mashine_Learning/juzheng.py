import numpy as np

# 从列表创建矩阵
matrix1 = np.array([[1, 2, 3],
                    [4, 5, 6],
                    [7, 8, 9]])
print("从列表创建:")
print(matrix1)

# 创建全零矩阵
zeros_matrix = np.zeros((3, 4))  # 3行4列
print("\n全零矩阵:")
print(zeros_matrix)

# 创建全1矩阵
ones_matrix = np.ones((2, 3))  # 2行3列
print("\n全1矩阵:")
print(ones_matrix)

# 创建单位矩阵
identity_matrix = np.eye(3)  # 3x3单位矩阵
print("\n单位矩阵:")
print(identity_matrix)

# 创建对角矩阵
diagonal_matrix = np.diag([1, 2, 3, 4])
print("\n对角矩阵:")
print(diagonal_matrix)