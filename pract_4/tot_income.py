

def main():
    incomes = []
    Month = int(input("How many months? "))

    for month in range(1, Month + 1):
        income = float(input("Enter income for month " + str(month) + ": "))
        incomes.append(income)

    print("\nIncome Report\n-------------")
    total = 0
    print_income(Month, incomes, total)


def print_income(Month, incomes, total):
    for mnth in range(1, Month + 1):
        income = incomes[mnth - 1]
        total += income
        print("Month {:2} - Income: ${:10.2f} Total: ${:10.2f}".format(mnth, income, total))


main()