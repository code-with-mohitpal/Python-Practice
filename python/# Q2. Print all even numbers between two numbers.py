# Q2. Print all even numbers between two numbers

def print_even(a, b):
    for i in range(a, b + 1):
        if i % 2 == 0:
            print(i)

print_even(2, 20)
