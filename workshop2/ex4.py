elements = input("Enter a list of elements separated by space: ").split()
consecutive_unique_elements = []

last_n = ""
for n in elements:
    if last_n != n:
        consecutive_unique_elements.append(n)
    last_n = n

print(f"\ninput: {elements}")
print(f"output: {consecutive_unique_elements}")
