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
            pass
        elif choice == "S":
            pass
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


main()