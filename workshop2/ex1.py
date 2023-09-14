nums = input("Enter a list of numbers separated by space: ").split()

for i in range(len(nums)):
    num = nums[i]
    if not (num.isdigit() or num.startswith("-") and num[1:].isdigit()):
        print("Error: input must be a list of numbers.")
        break
    nums[i] = int(num)
else:
    max = nums[0]
    for num in nums:
        if num > max:
            max = num

    print(f"\ninput: {nums}")
    print(f"output: {max}")
