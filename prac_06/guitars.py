"""
Estimate time: 20 minutes
Actual time: 40 minutes
"""
from prac_06.guitar import Guitar

guitars = []
print("My guitars!")
name =input("Name: ")
while name !='':
    year = int(input("Year: "))
    cost = float(input("Cost:$ "))
    guitar = Guitar(name,year,cost)
    print(f"{guitar} added")
    guitars.append(guitar)
    print()
    name = input("Name: ")
print("... snip ...")
print("These are my guitars:")
i = 0
for guitar in guitars:
    if guitar.is_vintage():
        print(f"Guitar {i+1}: {guitar} ({guitar.year}), worth ${guitar.cost} (vintage)")
    else:
        print(f"Guitar {i+1}: {guitar} ({guitar.year}), worth ${guitar.cost}")
    i+=1