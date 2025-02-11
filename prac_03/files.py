# 1.
out_file = open("name.txt","w")
name = input("Enter your name: ")
print(name, file=out_file)
out_file.close()
# 2.
in_file = open("name.txt","r")
input_name = in_file.read().strip()
in_file.close()
print(f"Hi {input_name}!")
# 3.
with open("numbers.txt","r") as numbers:
    first_number = int(numbers.readline().strip())
    second_number = int(numbers.readline().strip())
    print(first_number + second_number)
# 4
with open("numbers.txt","r") as numbers:
    total = 0
    numbers = numbers.readlines()
    for number in numbers:
        number.strip()
        total += int(number)
    print(total)