# Q7. Positive or Negative until user enters Quit

while True:
    value = input("Enter a number or Quit: ")

    if value == "Quit":
        break

    num = int(value)

    if num > 0:
        print("Positive")
    elif num < 0:
        print("Negative")
    else:
        print("Zero")
