def repeat(repeat_time):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(repeat_time):
                func(*args, **kwargs)
        return wrapper
    return decorator


@repeat(3)
def say_hello():
    print("hello")

say_hello()