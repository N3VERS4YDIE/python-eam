MIN_YEAR, MAX_YEAR = 1904, 2196
is_leap = False

while True:
    year = input(f"year between [{MIN_YEAR}, {MAX_YEAR}]: ")
    if year.strip().isdigit() and MIN_YEAR <= (year := int(year)) <= MAX_YEAR:
        break
    print("invalid year...\n")

IS_LEAP = year % 4 == 0 and year % 100 != 0 or year % 400 == 0
print(year + " is a ", "leap year ✨" if IS_LEAP else "common year 🤷")

# Alternative condition: not year % 4 and year % 100 or not year % 400
