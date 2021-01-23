from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# Creates the three items on the menu using the MenuItem class.
menu = Menu()

# Creates the Resource object.
coffee_machine = CoffeeMaker()

# Creates the Money object.
money = MoneyMachine()

# Variable used to turn machine off. Default is True
is_on = True

# Starts the program
while is_on:
    drink = {}
    choice = input("What would you like? (espresso/latte/cappuccino/): ")
    # off is a hidden choice.
    if choice == 'off':
        is_on = False
        print("\nTurning the Coffee Machine off.")
    # report is a hidden choice.
    elif choice == 'report':
        print('\nReport: ')
        coffee_machine.report()
        money.report()
    elif choice not in menu.get_items():
        print("I didn't understand your choice.")
    else:
        drink = menu.find_drink(choice)
        if coffee_machine.is_resource_sufficient(drink):
            if money.make_payment(drink.cost):
                coffee_machine.make_coffee(drink)
