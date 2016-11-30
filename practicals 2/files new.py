"""name = input("what's your name?:").title()
output_file = open("{}.txt".format(name),"w")
output_file.write(name)
output_file.close()

input_file = open("{}.txt".format(name),"r"))
for line in input_file:
    print("your name is",line)
input_file.close()

output_file2 = open("numbers.txt","w")
print(17,file = output_file2)
print(42,file = output_file2)
output_file2.close()"""

input_file2 = open("numbers.txt","r")
sum = 0
for line in input_file2:
    sum = sum + int(line)
print("The result is:",sum)
input_file2.close()