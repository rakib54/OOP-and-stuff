take_num = int(input("Enter your number: "))
nums_lst = [num for num in range(1, take_num+1)]

for i in range(1, take_num +1):
    for j in nums_lst:
        print(j, end="")
    if i != take_num:
        temp = nums_lst[i-1]
        nums_lst[i-1] = nums_lst[i]
        nums_lst[i] = temp
    print()
