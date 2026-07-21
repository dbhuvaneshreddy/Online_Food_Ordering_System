from menu import food
def generate_bill(order):
    total = 0
    print("\n-----BILL-----")
    for item,qty in order.items():
        amount = food[item]*qty
        total=total+amount
        print(item,"x",qty,"=",amount)
    print("-------------")
    print("Total Bill =,total")
    gst = total * 0.05
    print("Total Bill =",total)
    final_bill = total + gst
    print("Final_bill")
    return final_bill