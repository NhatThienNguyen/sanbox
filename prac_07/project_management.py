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
    incomplete_projects = check_complete_state(projects)
    print(projects)
    print(f"Welcome to Pythonic Project Management\nLoaded 5 projects from projects.txt\n{MENU}")
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "L":
            pass
        elif choice == "S":
            pass
        elif choice == "D":
            display_projects(projects, incomplete_projects)
        elif choice == "F":
            pass
        elif choice == "A":
            pass
        elif choice == "U":
            i = 0
            for project in incomplete_projects:
                print(f"{i} {project}")
                i += 1
            project_choice = get_valid_project_choice(incomplete_projects)
            print(incomplete_projects[project_choice])
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
            projects.sort()
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


def get_valid_project_choice(incomplete_projects):
    valid_state = False
    while not valid_state:
        try:
            choice = int(input("Project choice: "))
            if 0 <= choice < len(incomplete_projects):
                valid_state = True
            else:
                print("Out of range, choose other number")
        except ValueError:
            print("Invalid choice")
    return choice




main()