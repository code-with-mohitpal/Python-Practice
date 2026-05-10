try:
    num = int(input("Enter Number: "))
    result = 100 / num
    print(result)

except ZeroDivisionError:
    print("Cannot divide by zero")

except ValueError:
    print("Invalid input")

finally:
    print("Execution Completed")
