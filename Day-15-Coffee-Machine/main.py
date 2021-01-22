MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

money = 0.00
on = True


def start_machine():
    choice = input("What would you like? (espresso/latte/cappuccino):")
    if choice == 'espresso':
        verify_resources('espresso')
    elif choice == 'latte':
        verify_resources('latte')
    elif choice == 'cappuccino':
        verify_resources('cappuccino')
    elif choice == 'report':
        print("\nwater: {w}ml\nmilk: {m}ml\ncoffee: {c}gm\nmoney: ${d}".format(w=resources['water'], m=resources['milk'],
                                                           c=resources['coffee'], d=money))
    elif choice == 'off':
        global on
        on = False
        print("Turning off Coffee Machineo")
    else:
        print('I don\'t understand')


def payment(choice):
    coins = {'quarter': .25, 'dime': .10, 'nickle': .05, 'penny': .01}
    quarters = int(input("How many quarters to deposit? ")) * coins['quarter']
    dimes = int(input("How many dimes to deposit? ")) * coins['dime']
    nickles = int(input("How many nickles to deposit? ")) * coins['nickle']
    pennies = int(input("How many pennies to deposit? ")) * coins['penny']
    deposited = quarters + dimes + nickles + pennies
    if deposited >= MENU[choice]['cost']:
        global money
        money += MENU[choice]['cost']
        change = deposited - MENU[choice]['cost']
        print("Here is your {drink}. Enjoy!".format(drink=choice))
        print("Your change is {change}".format(change=change))
        global resources
        for i in MENU[choice]['ingredients'].keys():
            resources[i] = resources[i] - MENU[choice]['ingredients'][i]
    else:
        print("Sorry that's not enough money. Money refunded.")


def verify_resources(choice):
    available = []
    for i in MENU[choice]['ingredients'].keys():
        if MENU[choice]['ingredients'][i] > resources[i]:
            print('Sorry there is not enough {choice}.'.format(choice=i))
            available.append(MENU[choice]['ingredients'][i] <= resources[i])
        else:
            available.append(MENU[choice]['ingredients'][i] <= resources[i])
    if False not in available:
        payment(choice)


while on:
    start_machine()

