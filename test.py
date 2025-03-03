import csv
from operator import itemgetter

def main():
    countries_to_population ={}
    with open('countries.csv','r') as IN_FILE:
        countries_to_population = csv.DictReader(IN_FILE)
        for row in countries_to_population:
            print(countries_to_population['Country ('])



main()