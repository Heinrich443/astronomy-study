# 变量定义
x = 10           # 整数
y = 3.14         # 浮点数
name = "Alice"   # 字符串
is_active = True # 布尔值

# 多变量赋值
a, b, c = 1, 2, "three"

# 查看数据类型
# 内置的 type() 函数可以用来查询变量所指的对象类型。
print(type(x))              # <class 'int'>
print(type(y))              # <class 'float'>
print(type(name))           # <class 'str'>
print(type(is_active))      # <class 'bool'>
# 还可以用 isinstance() 来判断：
print(isinstance(a, int))   # True

# 数字类型
print(5 + 4)   # 加法
print(4.3 - 2) # 减法
print(3 * 7)   # 乘法
print(2 / 4)   # 除法，得到一个浮点数
print(2 // 4)  # 整除，得到一个整数
print(17 % 3)  # 取余
print(2 ** 5)  # 乘方

# Python 3 中整数字面量不允许前导零（如 080）
# 八进制数必须使用 0o 前缀（如 0o17）
print(0o12)
# 十六进制使用 0x 前缀（如 0x69）
print(0x12)
# 二进制使用 0b 前缀
print(0b11)

# 字符串类型
my_str = 'Runoob'       # 定义一个字符串变量（避免使用 str 作为变量名，会覆盖内置类型）
print(my_str)           # 打印整个字符串：Runoob
print(my_str[0:-1])     # 打印索引 0 到倒数第二个字符（不含最后一个）：Runoo
print(my_str[0])        # 打印第一个字符：R
print(my_str[2:5])      # 打印索引 2、3、4 的字符（不含索引 5）：noo
print(my_str[2:])       # 打印从索引 2 开始到末尾：noob
print(my_str * 2)       # 重复打印两次：RunoobRunoob
print(my_str + "TEST")  # 字符串拼接：RunoobTEST

# 布尔类型的值和类型
a = True
b = False
print(type(a))  # <class 'bool'>
print(type(b))  # <class 'bool'>

# 布尔类型的整数表现
print(int(True))   # 1
print(int(False))  # 0

# 使用 bool() 函数进行转换
print(bool(0))          # False
print(bool(42))         # True
print(bool(''))         # False
print(bool('Python'))   # True
print(bool([]))         # False
print(bool([1, 2, 3]))  # True

# 布尔逻辑运算
print(True and False)  # False
print(True or False)   # True
print(not True)        # False

# 布尔比较运算
print(5 > 3)   # True
print(2 == 2)  # True
print(7 < 4)   # False

# 布尔值在控制流中的应用
if True:
    print("This will always print")

if not False:
    print("This will also always print")

x = 10
if x:
    print("x 是非零值，在布尔上下文中为 True")

# 列表
my_list = ['abcd', 786, 2.23, 'runoob', 70.2]  # 避免使用 list 作为变量名，会覆盖内置类型
tinylist = [123, 'runoob']

print(my_list)             # 打印整个列表：['abcd', 786, 2.23, 'runoob', 70.2]
# 与 Python 字符串不一样的是，列表中的元素是可以改变的
my_list[1] = 999
print(my_list)             # 打印整个列表：['abcd', 999, 2.23, 'runoob', 70.2]
print(my_list[0])          # 打印第一个元素（索引 0）：abcd
print(my_list[1:3])        # 打印索引 1 和 2 的元素（不含索引 3）：[786, 2.23]
print(my_list[2:])         # 打印从索引 2 开始到末尾的所有元素：[2.23, 'runoob', 70.2]
print(tinylist * 2)        # 重复打印 tinylist 两次：[123, 'runoob', 123, 'runoob']
print(my_list + tinylist)  # 拼接两个列表

# 元组
my_tuple = ('abcd', 786, 2.23, 'runoob', 70.2)  # 避免使用 tuple 作为变量名
tinytuple = (123, 'runoob')

print(my_tuple)               # 输出完整元组
print(my_tuple[0])            # 输出第一个元素：abcd
print(my_tuple[1:3])          # 输出索引 1 和 2 的元素：(786, 2.23)
print(my_tuple[2:])           # 输出从索引 2 开始的所有元素
print(tinytuple * 2)          # 输出两次 tinytuple
print(my_tuple + tinytuple)   # 连接两个元组

# 构造包含 0 个或 1 个元素的元组比较特殊，有一些额外的语法规则
tup1 = ()    # 空元组
tup2 = (20,) # 一个元素，需要在元素后添加逗号
not_a_tuple = (42)  # 这是整数 42，不是元组。在没有逗号的情况下，Python 会将括号解释为数学运算中的括号

sites = {'Google', 'Taobao', 'Runoob', 'Facebook', 'Zhihu', 'Baidu'}

print(sites)   # 输出集合（无序，重复元素会被自动去掉）

# 成员测试
if 'Runoob' in sites:
    print('Runoob 在集合中')
else:
    print('Runoob 不在集合中')

# set 可以进行集合运算
a = set('abracadabra')
b = set('alacazam')

print(a)           # a 中的唯一字符
print(a - b)       # a 和 b 的差集（在 a 中但不在 b 中）
print(a | b)       # a 和 b 的并集（在 a 或 b 中）
print(a & b)       # a 和 b 的交集（同时在 a 和 b 中）
print(a ^ b)       # a 和 b 的对称差集（在 a 或 b 中，但不同时存在）

# 字典
my_dict = {}
my_dict['one'] = "1 - 菜鸟教程"
my_dict[2]     = "2 - 菜鸟工具"

tinydict = {'name': 'runoob', 'code': 1, 'site': 'www.runoob.com'}

print(my_dict['one'])       # 输出键为 'one' 的值
print(my_dict[2])           # 输出键为 2 的值
print(tinydict)             # 输出完整的字典
print(tinydict.keys())      # 输出所有键
print(tinydict.values())    # 输出所有值

# 构造函数 dict() 可以直接从键值对序列中构建字典
dict1 = dict([('Runoob', 1), ('Google', 2), ('Taobao', 3)])
dict2 = {x: x**2 for x in (2, 4, 6)}
dict3 = dict(Runoob=1, Google=2, Taobao=3)

print(dict1)
print(dict2)
print(dict3)

# bytes类型
x = b"hello"           # 使用 b 前缀创建 bytes 对象
print(x)               # b'hello'
print(type(x))         # <class 'bytes'>
print(x[0])            # 104（'h' 的 ASCII 值，bytes 元素是整数）
# 由于 bytes 类型是不可变的，修改操作需要创建一个新的 bytes 对象
y = x[1:3]          # 切片操作，得到 b'el'
z = x + b"world"    # 拼接操作，得到 b'helloworld'
print(y)            # b'el'
print(z)            # b'helloworld'
# bytes 类型中的元素是整数值，因此在进行比较操作时需要使用相应的整数值。可以用 ord() 函数将字符转换为对应的整数值
if x[0] == ord("h"):    # ord("h") 返回 104
    print("第一个元素是 'h'")

def reverseWords(input):
    list = input.split(" ")
    rlist = list[-1::-1]
    return " ".join(rlist)

if __name__ == "__main__":
    input = "How was your day"
    rw = reverseWords(input)
    print(rw)