a='Hello'
b='World'
print(b>a)
a = 100
b = 100
print(a is b)

def sum_numbers(*args):
    print(f"args的类型: {type(args)}")  # <class 'tuple'>
    print(f"args的值: {args}")
    return sum(args)

print(sum_numbers(1, 2, 3))        # args: (1, 2, 3), 结果: 6
print(sum_numbers(10, 20))         # args: (10, 20), 结果: 30
print(sum_numbers(5))              # args: (5,), 结果: 5
print(sum_numbers())               # args: (), 结果: 0

