def decorator_with_args(func):
    def wrapper(*args, **kwargs):
        print(f"函数 {func.__name__} 被调用，参数: {args}, {kwargs}")
        result = func(*args, **kwargs)
        print(f"函数执行完成，返回值: {result}")
        return result
    return wrapper

@decorator_with_args
def add(a, b):
    return a + b

@decorator_with_args
def greet(name, message="你好"):
    return f"{message}, {name}!"

# 测试
print(add(3, 5))
print(greet("小明", message="Hello"))

#类装饰器
class Timer:
    """计时器装饰器类"""

    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        import time
        start = time.time()
        result = self.func(*args, **kwargs)
        end = time.time()
        print(f"函数 {self.func.__name__} 执行时间: {end - start:.4f}秒")
        return result


@Timer
def slow_function():
    import time
    time.sleep(1)
    return "完成"


slow_function()