# Q10. Number Guessing Game
# Q10. Number Guessing Game

secret_number = 25

while True:

    guess = int(input("Guess the number: "))

    if guess > secret_number:
        print("Too high")

    elif guess < secret_number:
        print("Too low")

    else:
        print("Correct Guess")
        break
