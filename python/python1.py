# check palindrome or not
s=input("Enter a string: ")
rev=""
for ch in s:
    rev=ch+rev
if s==rev:
        print("it is a palindrome.")
else:
        print("it is not a palindrome.")

# avg of list
n=[2,4,6,8]
avg=sum(n)/len(n)
print("number :",avg)


list1=[2,3,4,5,6]
list2=[7,8,9,10]
result=list1+list2
result.sort
print("result: ",result)

list1=list(map(int,input("Enter first list1: ").split()))
list2=list(map(int,input("Enter second list2: ").split()))
result=list1+list2
result.sort
print("result: ",result)
