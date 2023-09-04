total_evens = total_odds = 0

print("Enter 0 to finish...\n")

while True:
    num = input("Enter a number: ")

    if num == "0":
        break
    if not num.isdigit():
        print("Invalid input...\n")
        continue

    evens = odds = 0
    for digit in num:
        if int(digit) % 2 == 0:
            evens += 1
        else:
            odds += 1

    total_evens += evens
    total_odds += odds
    print(f"number of evens: {evens}")
    print(f"number of odds: {odds}\n")

print(f"total number of evens: {total_evens}")
print(f"total number of odds: {total_odds}")
