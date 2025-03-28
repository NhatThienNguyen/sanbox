"""
Wimbledon
Estimate: 20 minutes
Actual: 1 hour
"""
import csv

FILENAME = "wimbledon.csv"

def main():
    champion_names, countries = load_data(FILENAME)
    champion_to_win = count_win(champion_names)
    display_champion_info(champion_to_win,countries)


def load_data(FILENAME):
    champion_names = []
    countries = set()
    with open(FILENAME, "r", encoding="utf-8-sig") as in_file:
        reader = csv.reader(in_file)
        next(reader)
        for record in reader:
            country = record[1]
            champion = record[2]
            champion_names.append(champion)
            countries.add(country)
    return champion_names, countries


def count_win(champion_names):
    champion_to_win = {}
    for champion in champion_names:
        if champion in champion_to_win:
            champion_to_win[champion] += 1
        else:
            champion_to_win[champion] = 1
    return champion_to_win


def display_champion_info(champion_to_win,countries):
    max_width = max((len(champion) for champion in champion_to_win.keys()))
    print("Wimbledon Champion")
    for champion, count in champion_to_win.items():
        print(f"{champion:{max_width}} {count}")
    print(f"These are {len(countries)} countries have won Wimbledon:")
    print(f", ".join(sorted(countries)))


main()