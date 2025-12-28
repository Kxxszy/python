import numpy as np


class SimplePointPredictor:
    def __init__(self):
        self.points = []

    def add_point(self, x, y):
        self.points.append((x, y))

    def predict_y(self, x):
        """用最小二乘法根据x预测y"""
        if len(self.points) < 2:
            return None

        x_data = [p[0] for p in self.points]
        y_data = [p[1] for p in self.points]

        # 线性回归：y = a + b*x
        A = np.vstack([x_data, np.ones(len(x_data))]).T
        b, a = np.linalg.lstsq(A, y_data, rcond=None)[0]

        return a + b * x

    def predict_x(self, y):
        """用最小二乘法根据y预测x"""
        if len(self.points) < 2:
            return None

        x_data = [p[0] for p in self.points]
        y_data = [p[1] for p in self.points]

        # 线性回归：x = a' + b'*y
        A = np.vstack([y_data, np.ones(len(y_data))]).T
        b, a = np.linalg.lstsq(A, x_data, rcond=None)[0]

        return a + b * y


# 简单使用示例
predictor = SimplePointPredictor()
points = [(1, 2), (2, 4), (3, 6)]
for x, y in points:
    predictor.add_point(x, y)

print(f"x=4 -> y={predictor.predict_y(4):.2f}")
print(f"y=8 -> x={predictor.predict_x(8):.2f}")