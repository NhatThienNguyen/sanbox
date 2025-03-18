"""
Estimate time: 20 minutes
Actual time:
"""
import csv
from prac_07.guitar import Guitar

FILE_NAME = "guitars.csv"


def main():
    guitars = get_data(FILE_NAME)
    guitars.sort()
    for guitar in guitars:
        print(guitar)
    choice = input("Do you want to have new guitar?(Y/N) ").upper()
    if choice == "Y":
        name = input("Name: ")
        cost = float(input("Cost: "))
        year = int(input("Year: "))
        guitar = Guitar(name, year, cost)
        guitars.append(guitar)
        print("New guitar has been added.")
    else:
        print("No change has been made")
    save_data(guitars, FILE_NAME)


def get_data(file_name):
    guitars = []
    with open(file_name) as in_file:
        reader = csv.reader(in_file)
        for row in reader:
            year = int(row[1])
            cost = float(row[2])
            guitar= Guitar(row[0], year, cost)
            guitars.append(guitar)
    return guitars


def save_data(guitars, file_name):
    with open(file_name, "w", encoding="utf-8", newline='') as out_file:
        writer = csv.writer(out_file, delimiter=',')
        for guitar in guitars:
            writer.writerow(guitar)


main()