DISCOUNT_THRESHOLD = 100
DISCOUNT_RATE = 0.1

number_of_items = int(input("Number of items: "))
total_price =0

while number_of_items <= 0:
    print("Invalid number of items")
    number_of_items = int(input("Number of items: "))

for i in range(number_of_items):
    price_of_items = float(input("Price of items: "))
    total_price += price_of_items

if total_price > DISCOUNT_THRESHOLD:
    total_price = total_price - (total_price * DISCOUNT_RATE)

print(f"Total price for {number_of_items} items is ${total_price:.2f}")