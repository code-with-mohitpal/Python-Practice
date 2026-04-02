balance = float(input("Enter balance: "))
withdraw = float(input("Enter withdrawal amount: "))

if withdraw > balance:
    print("Insufficient Balance")
else:
    balance -= withdraw
    print("Remaining Balance:", balance)
