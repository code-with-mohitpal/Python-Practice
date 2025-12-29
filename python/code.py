name=input("Enter name: ")
age=int(input("Enter age: "))
print(f"Hello {name},you are {age} years old")

a=int(input("Enter first number: "))
b=int(input("Enter second number: "))
print("sum:",a+b)
print("difference:",a-b)
print("product:",a*b)
print("quotient:",a/b)


#average
a=int(input("Enter first integer: "))
b=int(input("Enter second integer: "))
c=float(input("Enter float number: "))
a=float(a)
b=float(b)
average=(a+b+c)/3
print("average: ",average)

user_str=(input("Enter number: "))
user_int=int(user_str)
user_float=float(user_str)
user_str_again=str(user_str)
print("integer: ",type(user_int))
print("float: ",type(user_float))
print("user_str_again: ",type(user_str_again))

x=10+3*2**2
print(x)

a=int(input("enter first number:" ))
b=int(input("enter second number: "))
# swap
temp=a
a=b
b=temp
print("a= ",a)
print("b= ",b)

#convert celsius to fahrenheit
celsius_input=input("Enter temperature in Celsius: ")
celsius_temp=float(celsius_input)
fahrenheit_temp=(celsius_temp*(9/5))+32
print(f"Temperature in Fahrenheit: {fahrenheit_temp}")

#decimal






r=float(input("Enter radius: "))
pi=3.14
area= 3.14*r*r
print("arae: ",area)

p=float(input("enter p values: "))
r=float(input("enter r values: "))
t=float(input("enter t values: "))
si=(p*r*t)/100
print("SI: ",si)
