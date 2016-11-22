sales = float(input("Enter sales: $"))
while sales <= 0:
    print("Invalid option")
    sales = float(input("Enter sales: $"))
if sales < 1000:
    bonus = sales * 0.1
    print(bonus)
else:
    bonus = sales * 0.15
    print(bonus)
    print("good bye")