USERNAME = "root"
PASSWORD = "13"

tries = 3
while tries > 0:
    tries -= 1
    in_username = input("\nusername: ").strip()
    in_password = input("password: ").strip()
    if (in_username, in_password) == (USERNAME, PASSWORD):
        print("✅ successful login: correct username and password")
        break
    if tries == 0:
        print("❌ too many tries: you have been banned!")
        break
    print("❗ try again: incorrect ", end="")
    if in_username != USERNAME and in_password != PASSWORD:
        print("username and password")
    else:
        print("username" if in_username != USERNAME else "password")

# Warning: use getpass() instead of input() to get the password from the terminal
