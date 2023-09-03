while True:
    input = input("Enter a number: ")
    if input.isdigit():
        break
    print("Invalid input...\n")

output = input.replace("0", "zero-").replace("1", "one-").replace("2", "two-").replace("3", "three-").replace("4", "four-").replace("5", "five-").replace("6", "six-").replace("7", "seven-").replace("8", "eight-").replace("9", "nine-")

print(output[:-1])
