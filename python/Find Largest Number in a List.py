nums = list(map(int, input("Enter numbers: ").split()))

largest = nums[0]

for num in nums:
    if num > largest:
        largest = num

print("Largest number:", largest)
