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
            incomplete_projects = check_complete_state(projects)
            display_projects(projects, incomplete_projects)
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
        for line in data[1:]:
            line = line.replace("\n", "").replace("\t", ", ").split(",")
            priority = int(line[2])
            cost = float(line[3])
            completion = int(line[4])
            project = Project(line[0], line[1], priority, cost, completion)
            projects.append(project)
    return projects


def display_projects(projects,incomplete_projects):
    print("Incomplete projects:")
    for project in incomplete_projects:
        print(f"\t{project}")
    print("Complete projects:")
    for project in projects:
        if project not in incomplete_projects:
            print(f"\t{project}")


def check_complete_state(projects):
    incomplete_projects = []
    for project in projects:
        if project.complete < 100:
            incomplete_projects.append(project)
    return incomplete_projects


main()