def log_class(cls):
    class Wrapper:
        def __init__(self, *args, **kwargs):
            self.wrapped = cls(*args, **kwargs)

        def __getattr__(self, name):
            return getattr(self.wrapped, name)

        def display(self):
            print("before function calling")
            self.wrapped.display()
            print("after function calling")

    return Wrapper

@log_class
class MyClass:
    def display(self):
        print("original function executing")

obj = MyClass()
obj.display()