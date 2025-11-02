import numpy as np
import matplotlib.pyplot as plt


class NeuralNetwork:
    def __init__(self, layers, learning_rate=0.01):
        """
        初始化神经网络

        参数:
        layers: 列表，包含每层的神经元数量，例如[2, 4, 1]表示输入层2个神经元，隐藏层4个神经元，输出层1个神经元
        learning_rate: 学习率
        """
        self.layers = layers
        self.learning_rate = learning_rate
        self.parameters = {}

        # 初始化权重和偏置
        for i in range(1, len(layers)):
            self.parameters[f'W{i}'] = np.random.randn(layers[i - 1], layers[i]) * 0.1
            self.parameters[f'b{i}'] = np.zeros((1, layers[i]))

    def sigmoid(self, x):
        """Sigmoid激活函数"""
        return 1 / (1 + np.exp(-np.clip(x, -250, 250)))  # 防止数值溢出

    def sigmoid_derivative(self, x):
        """Sigmoid函数的导数"""
        return x * (1 - x)

    def forward_propagation(self, X):
        """前向传播"""
        self.cache = {'A0': X}

        # 输入层到隐藏层
        for i in range(1, len(self.layers)):
            Z = np.dot(self.cache[f'A{i - 1}'], self.parameters[f'W{i}']) + self.parameters[f'b{i}']
            A = self.sigmoid(Z)
            self.cache[f'Z{i}'] = Z
            self.cache[f'A{i}'] = A

        return self.cache[f'A{len(self.layers) - 1}']

    def compute_loss(self, y_pred, y_true):
        """计算损失（二元交叉熵）"""
        m = y_true.shape[0]
        # 添加小值防止log(0)
        loss = -np.mean(y_true * np.log(y_pred + 1e-8) + (1 - y_true) * np.log(1 - y_pred + 1e-8))
        return loss

    def backward_propagation(self, y_true):
        """反向传播"""
        m = y_true.shape[0]
        grads = {}

        L = len(self.layers) - 1  # 输出层索引

        # 输出层的误差
        dA = -(y_true / (self.cache[f'A{L}'] + 1e-8) -
               (1 - y_true) / (1 - self.cache[f'A{L}'] + 1e-8))

        for i in range(L, 0, -1):
            dZ = dA * self.sigmoid_derivative(self.cache[f'A{i}'])
            dW = np.dot(self.cache[f'A{i - 1}'].T, dZ) / m
            db = np.sum(dZ, axis=0, keepdims=True) / m

            if i > 1:  # 如果不是第一层，继续反向传播
                dA = np.dot(dZ, self.parameters[f'W{i}'].T)

            grads[f'dW{i}'] = dW
            grads[f'db{i}'] = db

        return grads

    def update_parameters(self, grads):
        """更新参数"""
        for i in range(1, len(self.layers)):
            self.parameters[f'W{i}'] -= self.learning_rate * grads[f'dW{i}']
            self.parameters[f'b{i}'] -= self.learning_rate * grads[f'db{i}']

    def train(self, X, y, epochs=1000, verbose=True):
        """训练神经网络"""
        losses = []

        for epoch in range(epochs):
            # 前向传播
            y_pred = self.forward_propagation(X)

            # 计算损失
            loss = self.compute_loss(y_pred, y)
            losses.append(loss)

            # 反向传播
            grads = self.backward_propagation(y)

            # 更新参数
            self.update_parameters(grads)

            if verbose and epoch % 100 == 0:
                print(f"Epoch {epoch}, Loss: {loss:.4f}")

        return losses

    def __call__(self, X, threshold=0.5):
        """
        让神经网络实例可以像函数一样被调用
        例如: predictions = model(X_data)
        """
        # 前向传播获取预测概率
        probabilities = self.forward_propagation(X)

        # 根据阈值进行二分类
        predictions = (probabilities > threshold).astype(int)

        return predictions

    def predict_proba(self, X):
        """返回预测概率"""
        return self.forward_propagation(X)

    def accuracy(self, X, y):
        """计算准确率"""
        predictions = self(X)  # 使用 __call__ 方法
        return np.mean(predictions == y)


# 测试代码
if __name__ == "__main__":
    # 设置随机种子以确保结果可重现
    np.random.seed(42)

    # 生成示例数据（异或问题）
    X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
    y = np.array([[0], [1], [1], [0]])

    print("输入数据:")
    print("X:", X)
    print("y:", y.flatten())

    # 创建神经网络实例
    nn = NeuralNetwork(layers=[2, 4, 1], learning_rate=0.5)

    print("\n开始训练...")
    # 训练神经网络
    losses = nn.train(X, y, epochs=2000, verbose=True)

    # 使用不同的方式进行预测
    print("\n预测结果:")

    # 使用 __call__ 方法
    predictions_call = nn(X)
    print(f"使用 __call__ 方法: {predictions_call.flatten()}")

    # 使用 predict_proba 方法
    probabilities = nn.predict_proba(X)
    print(f"预测概率: {probabilities.flatten()}")

    # 计算准确率
    accuracy = nn.accuracy(X, y)
    print(f"准确率: {accuracy * 100:.2f}%")

    # 绘制损失曲线
    plt.figure(figsize=(10, 6))
    plt.plot(losses)
    plt.title('Training Loss')
    plt.xlabel('Epoch')
    plt.ylabel('Loss')
    plt.grid(True)
    plt.show()