"""
Estimate time: 1 hour
Actual time:
"""
from prac_07.project import Project
import datetime

MENU =("- (L)oad projects\n- (S)ave projects\n- (D)isplay projects\n- (F)ilter projects by date\n- (A)dd new project\n"
       "- (U)pdate projects\n- (Q)uit")
FILE_NAME ="projects.txt"


def main():
    projects = get_data(FILE_NAME)
    print(projects)
    print(f"Welcome to Pythonic Project Management\nLoaded 5 projects from projects.txt\n{MENU}")
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "L":
            pass
        elif choice == "S":
            pass
        elif choice == "D":
            pass
        elif choice == "F":
            pass
        elif choice == "A":
            pass
        elif choice == "U":
            pass
        print(MENU)
        choice = input(">>> ").upper()


def get_data(file_name):
    projects =[]
    with open(file_name, "r") as in_file:
        data = in_file.readlines()
        for line in data:
            line = line.strip().replace("\n", "").replace("\t", ", ")
            projects.append(line)
        projects.remove(projects[0])
    return projects


main()