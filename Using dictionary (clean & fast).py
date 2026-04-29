def calculator(op, a, b):
    operations = {
        "add": a + b,
        "sub": a - b,
        "mul": a * b,
        "div": a / b
    }
    return operations.get(op, "Invalid operation")

print(calculator("div", 20, 4))
