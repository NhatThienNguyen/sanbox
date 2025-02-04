MENU = "(G)et valid score\n(P)rint result\n(S)how stars\n(Q)uit"

def main():
    score = int(input("Enter your score: "))
    valid_score = validate_score(score)
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "G":
            score = int(input("Enter your score: "))
            valid_score = validate_score(score)
        elif choice == "P":
            result = check_grade(valid_score)
            print(f"Your result is {result}")
        elif choice == "S":
            print(valid_score*"*")
        else:
            print("Invalid choice")
        print(MENU)
        choice = input(">>> ").upper()
    print("farewell")


def validate_score(score):
    while score < 0 or score > 100:
        print("Invalid score")
        score = int(input("Enter your score: "))
    return score


def check_grade(valid_score):
    if valid_score >= 90:
        return "Excellent"
    elif valid_score >= 50:
        return "Passable"
    else:
        return "Bad"


main()