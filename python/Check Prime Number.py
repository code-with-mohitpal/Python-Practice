num = int(input("Enter number: "))
flag = True

if num <= 1:
    flag = False
else:
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            flag = False
            break

if flag:
    print("Prime number")
else:
    print("Not prime")
