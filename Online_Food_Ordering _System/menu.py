food = {
    "pizza":200,
    "Burger":120,
    "Biriyani":250,
    "Cool Drink":50
}
def show_menu():
    print("------MENU------")
    for item,price in food.items():
        print(item,"-",price)