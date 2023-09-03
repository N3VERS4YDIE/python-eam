from math import log10

while True:
    num = input("Enter a number: ")
    if num.isdigit() and (num := int(num)) >= 10:
        break
    print("Invalid input...\n")

max_digit = max_pos = 0
n = int(log10(num)) + 1
for i in range(n):
    if (digit := num % 10) >= max_digit:
        max_digit = digit
        max_pos = n - i
    num //= 10

print(f"Largest digit {max_digit}, position {max_pos}")
