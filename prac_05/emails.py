"""
Email
Estimate: 20 minutes
Actual:
"""
def main():
    email_to_name = {}
    email = input('Enter your email: ').strip()
    while email != "":
        name = extract_name(email)
        choice = input(f"Is your name {name}? (Y/N) ").upper()
        if choice == "Y" or choice =="":
            email_to_name[email] = name
        else:
            name = input("Enter your name: ").title()
            email_to_name[email] = name
        email = input('Enter your email: ').strip()


def extract_name(email):
    name = email.split('@')[0].replace('.', ' ').title()
    return name


main()