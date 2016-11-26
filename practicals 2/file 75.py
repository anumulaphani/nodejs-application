"""output_file = open("name.txt","w")
output_file.write("enter your name")
output_file.close()

input_file = open("name.txt", "r")
for line in input_file:
    print(line)

output_file = open("numbers.txt","w")
output_file.write("enter the numbers")
output_file.close()"""

input_file = open("numbers.txt", "r")
for line in input_file:
    print(line)