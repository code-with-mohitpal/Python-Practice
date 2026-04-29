def calculator(op, a, b):
    match op:
        case "add":
            return a + b
        case "sub":
            return a - b
        case "mul":
            return a * b
        case "div":
            return a / b
        case _:
            return "Invalid operation"

print(calculator("mul", 4, 6))
