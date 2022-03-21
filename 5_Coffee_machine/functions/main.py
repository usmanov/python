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


def order(drink):
    resources['water'] -= MENU[drink]["ingredients"]["water"]
    resources['milk'] -= MENU[drink]["ingredients"]["milk"]
    resources['coffee'] -= MENU[drink]["ingredients"]["coffee"]


def report():
    print(f"Water: {resources['water']} ml\n"
          f"Milk: {resources['milk']} ml\n"
          f"Coffee: {resources['coffee']} g\n")


def is_resources_sufficient(drink):
    is_ok = 1
    if resources['water'] < MENU[drink]["ingredients"]["water"]:
        print("Sorry there is not enough water.")
        is_ok = 0
    if resources['milk'] < MENU[drink]["ingredients"]["milk"]:
        print("Sorry there is not enough milk.")
        is_ok = 0
    if resources['coffee'] < MENU[drink]["ingredients"]["coffee"]:
        print("Sorry there is not enough coffee.")
        is_ok = 0
    return is_ok


def money_machine():
    quarters = float(input("Quarters: "))
    dimes = float(input("Dimes: "))
    nickles = float(input("Nickles: "))
    pennies = float(input("Pennies: "))
    money = 0.25 * quarters + 0.1 * dimes + 0.05 * nickles + 0.01 * pennies
    return money


end = False
while not end:
    answer = input("What would you like? (espresso/latte/cappuccino/):")
    if answer == 'off':
        end = True
    elif answer == 'report':
        report()
    else:
        if is_resources_sufficient(answer) == 1:
            if money_machine() < MENU[is_resources_sufficient(answer)]["cost"]:
                print("Sorry that's not enough money. Money refunded.")
            elif money_machine() >= MENU[is_resources_sufficient(answer)]["cost"]:
                if money_machine() == MENU[is_resources_sufficient(answer)]["cost"]:
                    order(answer)
                    print(f"Here is your {MENU[is_resources_sufficient(answer)]} ☕️. Enjoy!")
                else:
                    change = money_machine() - MENU[is_resources_sufficient(answer)]["cost"]
                    print(f"Here is ${change} dollars in change.")
                    order(answer)
                    print(f"Here is your {MENU[is_resources_sufficient(answer)]} ☕️. Enjoy!")