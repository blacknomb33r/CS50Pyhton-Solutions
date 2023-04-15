
while True:
    amountDue = 50
    print("Amount Due:", amountDue)

    while amountDue > 0:
        coin = int(input("Insert Coin: "))
        if coin in [5, 10, 25]:
            amountDue -= coin
        else:
            pass
        if amountDue > 0:
            print("Amount Due:", amountDue)
        else:
            pass
    if amountDue == 0:
        print("Change Owed: 0")
        break
    elif amountDue < 0:
        print("Change Owed:", abs(amountDue))
        break
