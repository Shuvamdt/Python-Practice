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
    "coffee": 100
}
def report():
    key_list = resources.keys()
    print(f"{key_list[0].title()}: {resources[key_list[0]]}ml")
    print(f"{key_list[1].title()}: {resources[key_list[1]]}ml")
    print(f"{key_list[2].title()}: {resources[key_list[2]]}")

