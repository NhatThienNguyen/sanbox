"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""
import random


def main():
    score = float(input("Enter score: "))
    result = check_grade(score)
    print(result)
    score = random.randint(1, 100)
    result = check_grade(score)
    print(result)


def check_grade(score):
    if score < 0 or score > 100:
        return "Invalid score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"


main()
# Test value: 89,90,91,49,50,51