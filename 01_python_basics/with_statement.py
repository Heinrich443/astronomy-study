import decimal
import sqlite3
import threading
import time
from contextlib import contextmanager

# file
# 同时打开多个文件
with open('input.txt', 'r') as infile, open('output.txt', 'w') as outfile:
    content = infile.read()
    outfile.write(content)

# db
with sqlite3.connect('database.db') as conn:
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM users')
    results = cursor.fetchall()
# 连接自动关闭

# thread lock
lock = threading.Lock
with lock:
    # 临界区代码
    print('这段代码是线程安全的')

# temporarily modify system status
with decimal.localcontext() as ctx:
    ctx.prec = 42       # 临时设置高精度
    # 执行高精度计算
# 精度恢复原设置

# create custom context manager
# by defining __enter__ and __exit__
class Timer:
    def __enter__(self):
        self.begin = time.time()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.end = time.time()
        print(f"Time Consuming: {self.end - self.begin:.2f}")
        return False

with Timer() as t:
    sum(range(10000000))

# by contextlib
@contextmanager
def tag(name):
    print(f'<{name}>')
    yield
    print(f'</{name}>')

with tag('h1'):
    print('This is a title')