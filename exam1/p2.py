NUMS = input("Enter the numbers separated by comma: ")

str_num = ""
n = mean = std_deviation = 0
for char in NUMS + ",":
    if char == ",":
        n += 1
        num = float(str_num)
        mean += num
        std_deviation += num**2
        str_num = ""
    else:
        str_num += char

mean /= n
std_deviation = (std_deviation/n - mean**2)**(1/2)

print("mean: ", round(mean, 2))
print("standard deviation: ",  round(std_deviation, 2))
