import sys


def countdown(n):
    while n > 0:
        yield n
        n -= 1


def fabonacci(n):
    a, b, cnt = 0, 1, 0
    while cnt < n:
        yield a
        a, b = b, a + b
        cnt += 1

# countdown usage
# 创建生成器对象
it = iter(countdown(10))

# 通过迭代生成器获取值
print(next(it))
print(next(it))
print(next(it))

# 使用 for 循环迭代生成器
for i in it:
    print(i)

# fabonacci usage
f = fabonacci(5)
while True:
    try:
        print(next(f), end=" ")
    except StopIteration:
        sys.exit()