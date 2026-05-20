# Q8. Simple Calculator

def calculator(a, b, operation):

    if operation == '+':
        return a + b

    elif operation == '-':
        return a - b

    elif operation == '*':
        return a * b

    elif operation == '/':
        return a / b

    else:
        return "Invalid Operation"

print(calculator(10, 5, '+'))
print(calculator(10, 5, '-'))
print(calculator(10, 5, '*'))
print(calculator(10, 5, '/'))
