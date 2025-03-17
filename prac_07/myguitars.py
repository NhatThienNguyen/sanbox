"""
Estimate time: 20 minutes
Actual time:
"""
import csv
from prac_07.guitar import Guitar

IN_FILE = "guitars.csv"


def main():
    guitars = get_data()



def get_data():
    guitars = []
    with open(IN_FILE) as in_file:
        reader = csv.reader(in_file)
        for row in reader:
            guitars.append(row)
    return guitars