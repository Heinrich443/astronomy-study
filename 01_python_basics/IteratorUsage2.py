# 创建一个返回数字的迭代器，初始值为 1，逐步递增 1
class NumberAdder:
    def __iter__(self):
        self.a = 1
        return self

    # def __next__(self):
    #     x = self.a
    #     self.a += 1
    #     return x

    # 在 20 次迭代后停止执行
    def __next__(self):
        if self.a <= 20:
            x = self.a
            self.a += 1
            return x
        else:
            raise StopIteration


num = NumberAdder()
it = iter(num)

print(next(it))
print(next(it))
print(next(it))
print(next(it))

# 在 20 次迭代后停止执行
it = iter(num)
for i in it:
    print(i)