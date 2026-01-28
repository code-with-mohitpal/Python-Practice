#sum of digits
def sum_of_digits(n):
    total=0
    while n>0:
        total +=n%10
        n//=10
    return total
n=int(input("Enter number: "))
print("Sum of digits: ",sum_of_digits(n))