def check_permission(status):
    match status:
        case 200:
            return "OK - 请求成功"
        case 301 | 302:
            return "Redirect - 重定向"
        case 401 | 403 | 404:
            return "Not allowed - 无权限或未找到"
        case 500 | 502 | 503:
            return "Server Error - 服务器错误"
        case _:
            return "Unknown status - 未知状态码"


def match_example(item):
    match item:
        case (x, y) if x == y:
            print(f"匹配到相等的元组:{item}")
        case (x, y):
            print(f"匹配到元组: {item}")
        case _:
            print("匹配到其他情况")


class Circle:
    def __init__(self, radius):
        self.radius = radius


class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height


def match_shape(shape):
    match shape:
        case Circle(radius=1):
            print("匹配到半径为1的圆")
        case Rectangle(width=1, height=2):
            print("匹配到宽度为1，高度为2的矩形")
        case _:
            print("匹配到其他形状")


# call check_permission
for code in [200, 301, 403, 500, 418]:
    print(f"状态码 {code}: {check_permission(code)}")

# call match_example
match_example((1, 1))  # 输出: 匹配到相等的元组: (1, 1)
match_example((1, 2))  # 输出: 匹配到元组: (1, 2)
match_example("other") # 输出: 匹配到其他情况

match_shape(Circle(radius=1))          # 输出: 匹配到半径为1的圆
match_shape(Rectangle(width=1, height=2)) # 输出: 匹配到宽度为1，高度为2的矩形
match_shape("other")                    # 输出: 匹配到其他形状
