#1 tax rate calculation
def calculation_tax(salary):
    if salary < 30000:
        tax=0.05
    elif 30000<=salary<=70000:
        tax=0.15
    else:
        tax=0.25
    return tax
salary=int(input("Enter salary: "))
print("Final tax rate: ",calculation_tax(salary)*100,"%")


#2 print even number between a and b
def print_even(a,b):
    for i in range(a,b+1):
        if i%2==0:
            print(i,end=" ")
a=int(input("Enter a: "))
b=int(input("Enter b: "))
print_even(a,b)

#print odd number between a and b
def print_odd(a,b):
    for i in range(a,b+1):
        if i%2 !=0:
            print(i,end=" ")
a=int(input("Enter a: "))
b=int(input("Enter b: "))
print_odd(a,b)

#print digits of a number
def print_digits(n):
    while n>0:
        digit=n%10
        print(digit)
        n//=10
n=int(input("enter number: "))
print_digits(n)

#count number of digits
def count_digits(n):
    count=0
    while n>0:
        n//=10
        count +=1
    return count
n=int(input("enter number: "))
print("Number of digits: ",count_digits(n))

#sum of digits
def sum_of_digits(n):
    total=0
    while n>0:
        total +=n%10
        n//=10
    return total
n=int(input("Enter number: "))
print("Sum of digits: ",sum_of_digits(n))

#divisible by 3 and 5 (1 to 100)
for i in range(1,101):
    if i%3==0 & i%5==0:
        print(i,end=" ")
