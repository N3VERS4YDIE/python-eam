while True:
    age = input("Enter your age: ")
    if age.isdigit():
        break
    print("Invalid input...\n")
age = int(age)

vip_purchased = platinum_purchased = general_purchased = 0
while True:
    option = input(
        "\nSelect the ticket type number you want to add for purchase (enter any other value to finish):\n1. VIP\n2. Platinum\n3. General\n: ")
    if not option.isdigit() or (ticket_type := int(option)) < 1 or ticket_type > 3:
        break

    while True:
        quantity = input(f"\nEnter the number of type {option} tickets you want to purchase: ")
        if quantity.isdigit():
            break
        print("Invalid input...\n")

    quantity = int(quantity)
    if ticket_type == 1:
        vip_purchased += quantity
    elif ticket_type == 2:
        platinum_purchased += quantity
    else:
        general_purchased += quantity

VIP_PRICE = 80
PLATINUM_PRICE = 50
GENERAL_PRICE = 25

total_cost = GENERAL_PRICE * general_purchased
discount = 0

if age < 18:
    total_cost += 0.8 * VIP_PRICE * vip_purchased
    discount += 0.2 * VIP_PRICE * vip_purchased
else:
    total_cost += VIP_PRICE * vip_purchased

if platinum_purchased >= 6:
    total_cost += 0.95 * PLATINUM_PRICE * platinum_purchased
    discount += 0.05 * PLATINUM_PRICE * platinum_purchased
elif platinum_purchased > 10:
    total_cost += 0.9 * PLATINUM_PRICE * platinum_purchased
    discount += 0.1 * PLATINUM_PRICE * platinum_purchased

print(f"\nTotal cost: ${total_cost}\nTotal discount: ${discount}\nNumber of tickets purchased: {vip_purchased + platinum_purchased + general_purchased}\n")
