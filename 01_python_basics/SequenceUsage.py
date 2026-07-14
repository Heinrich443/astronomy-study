import operator
import time

# Python 中的序列类型包括字符串、列表（list）、元组（tuple）、字典（dict）和集合（set）

# string
# escape character
print('\'Hello, world!\'')  # 输出：'Hello, world!'

print("Hello, world!\nHow are you?")  # 输出：Hello, world!
                                        #       How are you?

print("Hello, world!\tHow are you?")  # 输出：Hello, world!    How are you?

print("Hello,\b world!")  # 输出：Hello world!

print("Hello,\f world!")  # 输出：
                           # Hello,
                           #  world!

print("A 对应的 ASCII 值为：", ord('A'))  # 输出：A 对应的 ASCII 值为： 65

print("\x41 为 A 的 ASCII 代码")  # 输出：A 为 A 的 ASCII 代码

decimal_number = 42
binary_number = bin(decimal_number)  # 十进制转换为二进制
print('转换为二进制:', binary_number)  # 转换为二进制: 0b101010

octal_number = oct(decimal_number)  # 十进制转换为八进制
print('转换为八进制:', octal_number)  # 转换为八进制: 0o52

hexadecimal_number = hex(decimal_number)  # 十进制转换为十六进制
print('转换为十六进制:', hexadecimal_number) # 转换为十六进制: 0x2a

time.sleep(0.1)

# 使用 \r 实现百分比进度：
for i in range(101): # 添加进度条图形和百分比
    bar = '[' + '=' * (i // 2) + ' ' * (50 - i // 2) + ']'
    print(f"\r{bar} {i:3}%", end='', flush=True)
    time.sleep(0.05)
print()

# string formatting
print ("我叫 %s 今年 %d 岁!" % ('小明', 10))

# list
list = ['ab', 'cd', 'ef', 'gh', 'ij']
list += ['kl']
print(list)

list.append('mn')
print(list)

del list[5]
print(list)

list.remove('cd')
print(list)

a = ['1', '2', '3', '4']
b = ['a', 'b', 'c', 'd']
c = ['a', 'b', 'c', 'd']
x = [a, b]
print(x)
print(x[0][1])

# list comparison
print(operator.eq(a, b))
print(operator.eq(b, c))

# list functions
print(len(x))
print(max(b))
c.reverse()
print(c)            # return c reverse
print(c.reverse())  # return None
list.sort()
print(list)         # return list sort
print(list.sort())  # return None

# tuple
tup = "a", "b", "c", "d"
print(type(tup))    # <class 'tuple'>

tup1 = ()
tup2 = (50, )
i = (50)
print(type(tup1))   # <class 'tuple'>
print(type(tup2))   # <class 'tuple'>
print(type(i))      # <class 'int'>

# dictionary
tinydict = {'Name': 'Runoob', 'Age': 7, 'Class': 'First'}
print(str(tinydict))    # {'Name': 'Runoob', 'Age': 7, 'Class': 'First'}
print(tinydict)         # {'Name': 'Runoob', 'Age': 7, 'Class': 'First'}

for i in tinydict.keys():
    print(i)

for item in tinydict.items():
    print(item)
    print(item[0])
    print(item[1])

for k in tinydict:
    print(k, end = '=') # key
    print(tinydict[k])  # value

# set
set1 = {1, 2, 3, 4}            # 直接使用大括号创建集合

list = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
basket = set(list)            # 使用 set() 函数从列表创建集合
print(basket)

a = set('abracadabra')
b = set('alacazam')
print("a = " + str(a))
print("b = " + str(b))
print("a - b = " + str(a - b))
print("a | b = " + str(a | b))
print("a & b = " + str(a & b))
print("a ^ b = " + str(a ^ b))

a = {x for x in 'abracadabra' if x not in 'abc'}
print(a)

# add
a.add('a')
print(a)
# update 可以添加元素，且参数可以是列表，元组，字典等
a.update({12, 23})
print(a)
a.update([1, 2], [2, 3])
print(a)