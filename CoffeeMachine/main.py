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

coins = {
    "pennies" : 0.01,
    "nickels" : 0.05,
    "dimes" : 0.10,
    "quarters" : 0.25
}
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100
}
money = 0
def coffee_machine():
    global money
    global resources
    def report():
        key_list = list(resources.keys())
        print(f"{key_list[0].title()}: {resources[key_list[0]]}ml")
        print(f"{key_list[1].title()}: {resources[key_list[1]]}ml")
        print(f"{key_list[2].title()}: {resources[key_list[2]]}g")
        print(f"Money : ${money}")

    choice = input("What would you like? (espresso/latte/cappuccino):").lower()
    if choice == "off" :
        return
    elif choice == "report":
        report()
    elif not choice in MENU :
        print("Service does not exist!")
        coffee_machine()
        return
    else:
        for key in MENU[choice]["ingredients"]:
            if resources[key] < MENU[choice]["ingredients"][key]:
                print(f"Sorry there is not enough {key}.")
                coffee_machine()
                return
        print("Please insert coins.")
        paid = 0
        for key in reversed(list(coins.keys())):
            paid += int(input(f"How many {key}?:")) * coins[key]

        price = MENU[choice]["cost"]
        if paid < price:
            print("Sorry that's not enough money. Money refunded.")
        else:
            for key in MENU[choice]["ingredients"]:
                resources[key] -= MENU[choice]["ingredients"][key]
            money += price
            if paid > price:
                print(f"Here is ${(paid - price).__round__(2)} dollars in change.")
            print(f"Here is your {choice} ☕ Enjoy!")
    coffee_machine()
coffee_machine()