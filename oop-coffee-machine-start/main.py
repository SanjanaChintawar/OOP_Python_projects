from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
from logo import logo

run_again = True
menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

print(logo)
while run_again:
    order = input(f"\n\t\tYour order? {menu.get_items()} : ")
    if order == "report":
        coffee_maker.report()
        money_machine.report()

    elif order == "off":
        run_again = False
    else:
        menu_item = menu.find_drink(order)
        drink_cost = menu_item.cost
        if coffee_maker.is_resource_sufficient(menu_item) and money_machine.make_payment(drink_cost):
            coffee_maker.make_coffee(menu_item)
