number = int(input("Enter a number: "))
nums = [val for val in range(1, number+1)]
for i in range(1, number+1):
    for j in nums:
        print(j, end="")
    if i != number:
        temp = nums[i-1]
        nums[i-1] = nums[i]
        nums[i] = temp
    print()
