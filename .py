n = int(input("Enter number: "))
temp = n
sum = 0

while n > 0:
    digit = n % 10
    sum += digit ** 3
    n //= 10

if sum == temp:
    print("Armstrong")
else:
    print("Not Armstrong")