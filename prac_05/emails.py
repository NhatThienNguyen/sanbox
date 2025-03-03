"""
Email
Estimate: 20 minutes
Actual: 25 minutes
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
    for email, name in email_to_name.items():
        print(f"{name} ({email})" )


def extract_name(email):
    """To extract name from email"""
    name = email.split('@')[0].replace('.', ' ').title()
    return name


main()