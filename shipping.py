num = int(input("Enter the number of items:"))
while num <=0:
    print("Invalid number")
    num = int(input("Enter the number of items:"))
price = 0
print(num)
amount = 0
print("Enter the amount for each item:")
for i in range(num):
    amount = int(input(">>>"))
    price = price + amount
if price >=100:
    discount = price * 0.1
    price = price - discount
print("Number of items:",num)
print("total shipping cost:",price)
