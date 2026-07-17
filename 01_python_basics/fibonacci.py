# 斐波那契(fibonacci)数列模块
def fib(n):     # 定义到 n 的斐波那契数列
    a, b, cnt = 0, 1, 0
    while cnt < n:
        print(b, end=" ")
        a, b = b, a + b
        cnt += 1
    print()

def fib2(n):  # 返回到 n 的斐波那契数列
    fibo = []
    a, b, cnt = 0, 1, 0
    while cnt < n:
        fibo.append(b)
        a, b = b, a + b
        cnt += 1
    return fibo