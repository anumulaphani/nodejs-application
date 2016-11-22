sales = float(input("Enter sales: $"))
if sales > 1000:
    bonus = sales * 0.15
    print("discount is ", (bonus))
else:
    bonus =sales * 0.1
    print("discount is", (bonus))