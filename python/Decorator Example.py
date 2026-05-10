# Decorator in Python

def smart_divide(func):
    def inner(a, b):
        if b == 0:
            print("Cannot divide by zero")
            return
        return func(a, b)
    return inner


@smart_divide
def divide(a, b):
    print(a / b)

divide(10, 2)
divide(10, 0)
