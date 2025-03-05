"""
Estimate time:
Actual time:
"""
from prac_06.guitar import Guitar

guitars = []
print("My guitars!")
name = Guitar(name=input("Name: "))
while name != '':
    year = Guitar(year=input("Year: "))
    cost = Guitar(cost=input("Cost: "))
    print(f"{name} ({year}): ${cost} added")
    guitars.append([name, year, cost])
    print()
    name = Guitar(name=input("Name: "))
print("... snip ...")
print("These are my guitars:")
i = 0
for guitar in guitars:
    if guitar[1].is_vintage():
        print(f"Guitar {i+1}: {guitar[0]} ({guitar[1]}), worth ${guitar[2]} (vintage)")
    else:
        print(f"Guitar {i+1}: {guitar[0]} ({guitar[1]}), worth ${guitar[2]}")