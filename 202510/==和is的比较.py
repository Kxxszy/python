x = 'abc'
z = 'c'
y = 'ab' + z
w = 'abc'
print(x == y)
print(x is y)
print(x is w)

spam = [1, 2, 3]
ham = spam
#del ham[0:3] #same del ham[0:3]
print(id(spam))
print(id(ham))
print(spam)

#spam=True
#print(spam=True)

_hello = "HelloWorld"
score_for_student = 0.0  # 没有错误发生
y = 20

name1 = "Tom"
name2 = "Tony"
a1 = 10
b1 = 20
print('{a1*b1}')


class Student:
    pass


print(Student.__module__)


class A:
    x = 10

    def foo(self): pass


print(A.__dict__)
