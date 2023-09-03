evens = 0
odds = 0

while True:
    nums = input("Enter a number: ")
    if nums == "0":
        break
    if not nums.isdigit():
        continue
    for num in nums:
        if int(num) % 2 == 0:
            evens += 1
        else:
            odds += 1

print(f"number of evens: {evens}")
print(f"number of odds: {odds}")
