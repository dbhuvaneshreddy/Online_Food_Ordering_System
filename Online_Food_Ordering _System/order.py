from menu import food
def take_order():
    order={}
    while True:
        item = input("Enter food name:")
        if item in food:
            qty = int(input("Enter quantity:"))
            order[item] = qty
        else:
            print("Item not available")
        ch = input("Add more?(yes/no):")
        if ch.lower() == "n0":
            break
        return order