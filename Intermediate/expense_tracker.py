expenses = []

while True:
    print("1. Add expense , 2. View all expenses , 3. Total spent , 4. Exit")
    c = int(input("choice: "))

    if c == 1:
        try:
            itm, amnt = input("Enter item name and expense separated by comma: ").split(",")
            dic = {"item": itm, "amount": int(amnt)}
            expenses.append(dic)
        except ValueError:
            print("Enter valid value")

    elif c == 2:
        if not expenses:
            print("empty")
        else:
            for i in expenses:
                print(i["item"], "-", i["amount"])

    elif c == 3:
        s = 0
        for i in expenses:
            s += i["amount"]
        print("sum:", s)

    elif c == 4:
        with open("expenses.txt", "w") as f:
            for i in expenses:
                f.write(f'{i["item"]},{i["amount"]}' + "\n")
        break
