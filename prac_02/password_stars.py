def main():
    password = get_password()
    print(len(password)* "*")


def get_password():
    password = input("Enter your password: ")
    while len(password) <= 0:
        print("Invalid password")
        password = input("Enter your password: ")
    return password


main()