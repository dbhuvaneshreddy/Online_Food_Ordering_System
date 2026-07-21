def make_payment(total):
    print("\n------PAYMENT------")
    print("1.Cash")
    print("2.UPI")
    print("3.CARD")
    choice = int(input("select payment Method:"))
    if choice == 1:
        print("Cash payment Selected")
    elif choice == 2:
        print("UPI payment Selected")
    elif choice == 3:
        print("Card payment Selected")
    else:
        print("Invalid option")
        return
    coupon = input("Enter Coupon Code or press Enter to skip):")
    if coupon == "SAVE50":
        total = total - 50
        print("Coupon Applied Successfully")
    else:
        print("No Coupon Applied")
    print("Amount to pay =",total)
    amount = float(input("Enter Amount:"))
    if amount == total:
        print("payment Successful")
    elif amount > total:
        print("payment Successful")
        print("Balance =",amount-total)
    else:
        print("Insufficient Amount")