"""
Estimate time: 1 hour
Actual time: 2 days and 3 Hours :)
"""
from prac_07.project import Project
import datetime

MENU =("- (L)oad projects\n- (S)ave projects\n- (D)isplay projects\n- (F)ilter projects by date\n- (A)dd new project\n"
       "- (U)pdate projects\n- (Q)uit")
FILE_NAME ="projects.txt"


def main():
    """Main function with interactive menu"""
    projects = get_data(FILE_NAME)
    print(projects)
    print(f"Welcome to Pythonic Project Management\nLoaded {len(projects)} projects from {FILE_NAME}\n{MENU}")
    choice = input(">>> ").upper()
    while choice != "Q":
        incomplete_projects = check_complete_state(projects)
        if choice == "L":
            projects = load_data()
            print(f"Loaded {len(projects)} projects from {FILE_NAME}")
        elif choice == "S":
            save_choice = input(f"Do you want to save to {FILE_NAME}? (y/n) ").upper()
            if save_choice == "Y":
                save_data(projects)
            else:
                print("No saving has been made")
        elif choice == "D":
            display_projects(projects, incomplete_projects)
        elif choice == "F":
            filer_datetime(projects)
        elif choice == "A":
            print("Let's add a new project")
            add_new_project(projects)
        elif choice == "U":
            i = 0
            for project in incomplete_projects:
                print(f"{i} {project}")
                i += 1
            project_choice = get_valid_project_choice(incomplete_projects)
            print(incomplete_projects[project_choice])
            new_percentage = get_valid_input("New Percentage: ")
            if new_percentage >= incomplete_projects[project_choice].complete and new_percentage !='':
                incomplete_projects[project_choice].complete = new_percentage
            new_priority = get_valid_input("New Priority: ")
            if new_priority != incomplete_projects[project_choice].priority and new_priority != '':
                incomplete_projects[project_choice].priority = new_priority
        print(MENU)
        choice = input(">>> ").upper()
    save_choice = input(f"Do you want to save to {FILE_NAME}? ").upper()
    if save_choice != "Y" or save_choice != "YES":
        print("Thank you for using custom-built project management software!")


def get_data(file_name):
    """Get data from file and convert it to list"""
    projects =[]
    with open(file_name, "r") as in_file:
        data = in_file.readlines()
        for line in data[1:]:
            line = line.replace("\n", "").replace("\t", ", ").split(",")
            line[1]= line[1].strip()
            date = datetime.datetime.strptime(line[1], "%d/%m/%Y").date()
            priority = int(line[2])
            cost = float(line[3])
            completion = int(line[4])
            project = Project(line[0], date, priority, cost, completion)
            projects.append(project)
            projects.sort()
    return projects


def display_projects(projects,incomplete_projects):
    """Display all the projects"""
    print("Incomplete projects:")
    for project in incomplete_projects:
        print(f"\t{project}")
    print("Complete projects:")
    for project in projects:
        if project not in incomplete_projects:
            print(f"\t{project}")


def check_complete_state(projects):
    """Checking for complete state of project, if not yet complete will be added to another list"""
    incomplete_projects = []
    for project in projects:
        if project.complete < 100:
            incomplete_projects.append(project)
    return incomplete_projects


def get_valid_project_choice(incomplete_projects):
    """Get valid project choice to make sure the index won't go out of range or not right input"""
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


def get_valid_input(prompt):
    """Get valid input from user"""
    new_input = input(prompt)
    if new_input !="":
        new_input=int(new_input)
    return new_input


def add_new_project(projects):
    """Add new project and save to the list"""
    name = input("Name: ")
    start_date = input("Start date (dd/mm/yy): ")
    start_date = datetime.datetime.strptime(start_date, "%d/%m/%Y").date()
    priority = int(input("Priority: "))
    cost = float(input("Cost estimate: $"))
    completion = int(input("Percent complete: "))
    project = Project(name, start_date, priority, cost, completion)
    projects.append(project)
    return projects


def update_projects(projects, incomplete_projects):
    """Update the projects list for project already have 100% completion"""
    for project in incomplete_projects:
        if project.complete == 100:
            projects.remove(project)
            projects.append(project)
    return projects


def filer_datetime(projects):
    """Convert to datetime and filter it"""
    input_date = input("Show projects that start after date (dd/mm/yy): ")
    input_date = datetime.datetime.strptime(input_date, "%d/%m/%Y").date()
    for project in projects:
        if project.date >= input_date:
            print(f"{project}")


def load_data():
    """Load data from user file"""
    projects = []
    valid_state = False
    while not valid_state:
        try:
            file_name = input("Load file: ")
            if ".txt" not in file_name:
                file_name = file_name+".txt"
            with open(file_name, "r") as in_file:
                data = in_file.readlines()
                valid_state = True
        except FileNotFoundError:
            print("File not found")
    for line in data[1:]:
        line = line.replace("\n", "").replace("\t", ", ").split(",")
        line[1] = line[1].strip()
        date = datetime.datetime.strptime(line[1], "%d/%m/%Y").date()
        priority = int(line[2])
        cost = float(line[3])
        completion = int(line[4])
        project = Project(line[0], date, priority, cost, completion)
        projects.append(project)
        projects.sort()
    return projects


def save_data(projects):
    """save data to file"""
    with open(FILE_NAME, "w") as out_file:
        for project in projects:
            out_file.write(f"{project.name} {project.date} {project.priority} {project.cost} {project.complete}\n")


main()