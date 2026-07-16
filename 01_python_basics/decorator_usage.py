def decorator_function(original_function):
    def wrapper(*args, **kwargs):
        # before function calling
        print("before executing")

        result = original_function(*args, **kwargs)

        # after function calling
        print("after executing")

        return result
    return wrapper

@decorator_function
def target_function():
    print("original function executing")


target_function()