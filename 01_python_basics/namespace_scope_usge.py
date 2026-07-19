num = 1

def func():
    global num
    print(num)
    num = 123
    print(num)

print(num)
func()
print(num)

def outer():
    num = 10
    def inner():
        nonlocal num   # nonlocal关键字声明
        num = 100
        print(num)
    inner()
    print(num)
outer()