irregular_matrix = []
print("Enter an element or a list of elements separated by space (empty to finish):")

i = 0
while True:
    i = i+1
    row = input(f"{i}: ").split()
    if len(row) == 0:
        break
    for j in range(len(row)):
        col = row[j]
        if col.isdigit() or col.startswith("-") and col[1:].isdigit():
            row[j] = int(col)
    if len(row) == 1:
        row = row[0]
    irregular_matrix.append(row)

vector = []
for row in irregular_matrix:
    if type(row) == list:
        for col in row:
            vector.append(col)
    else:
        vector.append(row)

print(f"\ninput: {irregular_matrix}")
print(f"output: {vector}")
