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
    if resources['water'] < MENU[drink]["ingredients"]["water"]:
        print("Sorry there is not enough water.")
    if resources['milk'] < MENU[drink]["ingredients"]["milk"]:
        print("Sorry there is not enough milk.")
    if resources['coffee'] < MENU[drink]["ingredients"]["coffee"]:
        print("Sorry there is not enough coffee.")


end = False
while not end:
    answer = input("What would you like? (espresso/latte/cappuccino/):")
    if answer == 'off':
        end = True
    elif answer == 'report':
        report()
    else:
        order(answer)
        is_resources_sufficient(answer)


