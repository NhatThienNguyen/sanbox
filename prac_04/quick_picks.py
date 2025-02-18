import random

LOWER_THRESHOLD = 1
UPPER_THRESHOLD = 45
RANDOM_NUMBERS = 6

quick_picks_number = int(input("How many quick picks? "))
for i in range(quick_picks_number):
    random_numbers = []
    while len(random_numbers) < RANDOM_NUMBERS:
        random_number = random.randint(LOWER_THRESHOLD, UPPER_THRESHOLD)
        if random_number not in random_numbers:
            random_numbers.append(random_number)
    random_numbers.sort()
    print(' '.join(f"{number:2}" for number in random_numbers))