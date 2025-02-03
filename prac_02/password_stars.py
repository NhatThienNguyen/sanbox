password = input("Enter your password: ")
while len(password) <= 0:
    print("Invalid password")
    password = input("Enter your password: ")
print(len(password)* "*")