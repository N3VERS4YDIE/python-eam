matrix = []
i = 1
print("Enter a row of numbers separated by space (empty to finish):")

while True:
    row = input(f"row {i}: ").split()
    if len(row) == 0:
        break
    for j in range(len(row)):
        col = row[j]
        if col.isdigit() or col.startswith("-") and col[1:].isdigit():
            row[j] = int(col)
        else:
            print("Error: row must be a list of numbers.\n")
            break
    else:
        matrix.append(row)
        i = i+1

sum = 0
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if i == j:
            sum += matrix[i][j]

print(f"\ninput: {matrix}")
print(f"output {sum}")
