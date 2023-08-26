NUMS_LEN = 5
nums = ""
i = sum = min = max = 0  # I'm shadowing built-in functions, but i'm not using them, so i think it's ok

while i < NUMS_LEN:
    nstr = input(f"number {i+1}: ")  # string number
    if not nstr.strip().removeprefix("-").isdigit():
        print("Invalid number...\n")
        continue
    n = int(nstr)  # integer number
    sum += n
    i += 1
    if i == 1:
        nums = nstr
        min = n
        max = n
    elif n > max or n == max:
        max = n
        nums = nstr + " " + nums
    elif n < min or n == min:
        min = n
        nums += " " + nstr
    else:
        nstr2 = ""  # string number, chars accumulator
        for char in nums + " ":
            if char == " ":
                if int(nstr2) < n:
                    NSTR_INDEX = (nums + " ").index(" " + nstr2 + " ")
                    nums = nums[:NSTR_INDEX] + " " + nstr + nums[NSTR_INDEX:]
                    break
                nstr2 = ""
            else:
                nstr2 += char

print(f"""
min: {min}
max: {max}
sum: {sum}
average: {sum/NUMS_LEN}
sorted numbers (descending order): {nums}""")

# Alternative for sorting numbers: sorted(nums.split())
