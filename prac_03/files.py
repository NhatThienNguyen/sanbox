out_file = open("name.txt","w")
name = input("Enter your name: ")
print(name, file=out_file)
out_file.close()