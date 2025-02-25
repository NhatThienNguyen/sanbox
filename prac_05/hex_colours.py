CODE_TO_COLOUR = {"Absolute Zero": "#0048ba", "Acid Green": "#b0bf1a", "AliceBlue": "#f0f8ff",
                  "Alizarin Crimson": "#e32636", "Amaranth": "#e52b50", "Amber": "#ffbf00", "Amethyst": "#9966cc",
                  "Apricot": "#fbceb1", "Aqua": "#00ffff", "Army Green":"#4b5320"}

colour_name = input("Enter colour name: ")
if colour_name == "aliceblue":
    colour_name = "AliceBlue"
else:
    colour_name.title()
while colour_name != "":
    try:
        print(f"{colour_name} is {CODE_TO_COLOUR[colour_name]}")
    except KeyError:
        print("No such colour")
    colour_name = input("Enter colour name: ").title()
    if colour_name == "aliceblue":
        colour_name = "AliceBlue"
    else:
        colour_name.title()
print("Farewell")