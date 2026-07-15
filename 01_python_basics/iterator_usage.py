import sys

list = ['a', 'b', 'c', '1', '2', '3']
it = iter(list)         # 创建迭代器对象
print(it)               # 返回迭代器对象
print(next(it))         # 输出迭代器的下一个元素
print(next(it))

a = [1, 2, 3, 4]
it = iter(a)

for i in it:
    print(i)            # 这里隐式调用了next(i)

b = ['ab', 'bc', 'cd', 'de']
it = iter(b)            # 不重新赋值则 while 循环中不会输出结果，因为迭代器
while True:
    try:
        print(next(it))
    except StopIteration:
        sys.exit()