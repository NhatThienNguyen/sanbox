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