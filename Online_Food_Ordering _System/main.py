from login import login
from menu import show_menu
from order import take_order
from bill import generate_bill
from payment import make_payment
history=[]
print("WELCOME TO ONLINE FOOD ORDERING SYSTEM")
if login():
    show_menu()
    order = take_order()
    history.append(order)
    total = generate_bill(order)
    make_payment(total)
    print("\n-----ORDER HISTORY------")
    for i in history:
        print(i)
    print("Thank you! Vist Again")
else:
    print("Access Denied")