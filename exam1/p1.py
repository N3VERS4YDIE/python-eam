cost = 300
VAT = 60

while True:
    km = input("Enter the kilometers traveled: ")
    if km.isdigit() and (km := int(km)) >= 1:
        break
    print("Enter a positive integer number >= 1\n")

if km > 300:
    cost += (km := km - 300) * 15
if km > 700:
    cost += (km - 700) * 10

print(f"cost: ${cost}")
print(f"VAT: ${VAT}")
print(f"total cost: ${cost + VAT}")
