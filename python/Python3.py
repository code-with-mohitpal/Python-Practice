
def divisible_by_3_and_5():
    for i in range(1,101):
        if i%3==0 & i%5==0:
            print(i,end=" ")
divisible_by_3_and_5()

#7 Quit
def check_number():
    while True:
        user_input=input("Enter a number or 'Quit' to stop: ")
        if user_input.lower()=="quit":
            print("Program stopped.")
            return
        n =int(user_input)
        if n>0:
            print("Positive number")
        elif n<0:
            print("Negative number")
        else:
            print("Zero")
check_number()


#calculator function
def calculator(a,b,operation):
    if operation=='+':
        return a+b
    elif operation=='-':
        return a-b
    elif operation=='*':
        return a*b
    elif operation=='/':
        if b!=0:
            return a/b
        else:
            return "Error: Division by zero"
    else:
        return "Invalid operation"
a=float(input("Enter first number: "))
b=float(input("Enter second number: "))
op=input("Enter operation(+,-,*,/):")
print("result: ",calculator(a,b,op))

#9 check if number is prime using loop
def is_prime(n):
    if n<=1:
        return False
    if n==2:
        return True
    for i in range(2,n):
        if n%i==0:
            return False
    return True
n=int(input("Enter a number: "))
print("Prime: ", is_prime(n))

 #10 number guessing game 
def number_guessing_game(secret_number):
    while True:
        guess=int(input("Guess the number: "))
        if guess>secret_number:
            print("Too high!")
        elif guess<secret_number:
            print("Too low!")
        else:
            print("Corrent!!")
            break
number_guessing_game(25)
