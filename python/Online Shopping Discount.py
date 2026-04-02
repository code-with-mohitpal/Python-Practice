amount = float(input("Enter purchase amount: "))

if amount >= 5000:
    discount = 0.20
elif amount >= 2000:
    discount = 0.10
else:
    discount = 0

final_price = amount - (amount * discount)

print("Final Price:", final_price)
