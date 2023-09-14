strings = input("Enter a list of elements separated by space: ").split()

unique_strings = []
for str in strings:
    if str not in unique_strings:
        unique_strings.append(str)

print(f"\ninput: {strings}")
print(f"output: {unique_strings}")