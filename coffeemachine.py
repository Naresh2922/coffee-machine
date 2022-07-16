import os
menu = {
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


def clear():
    command = 'clear'
    if os.name in ('nt', 'dos'):
        command = 'cls'
    os.system(command)


def get_value(ke, from_data):
    for key, value in from_data.items():
        if ke == key:
            return value


def money_input():
    quarters = int(input("quarters: "))
    dimes = int(input("dimes: "))
    nickels = int(input("nickels: "))
    pennies = int(input("pennies: "))
    total = quarters * 0.25 + dimes * 0.10 + nickels * 0.05 + pennies * 0.01
    return total

is_on = True
while is_on:
    def subtract():
        print(f"resources before purchase {drink}")
        for x, y in resources.items():
            print(f"{x} : {y}ml")
        print(f"resources after purchase {drink}")
        for i in requirements:
            resources[i] = get_value(i, resources) - get_value(i, requirements)
        for x, y in resources.items():
            print(f"{x} : {y}ml")
    drink = input("what would you like latte/espresso/cappuccino: ")
    requirements = menu[drink]["ingredients"]
    price = menu[drink]["cost"]
    if drink == "off":
        is_on = False
    elif drink == "report":
        for x, y in resources.items():
            print(f"{x} : {y}ml")
            
    res_available = True
    for i in requirements:
        if res_available:
            if get_value(i, resources) < get_value(i, requirements):
                print(f"Sorry there is not enough '{i}'")
                res_available = False
                is_on = False
    if res_available:
        print(f"Please insert coins of value {price}$ for {drink}")
        value = money_input()
        money_sufficient = False
        while value <= price and not money_sufficient:
            if input("insufficient amount. To add money type 'y' or For refund type 'r': ").lower() == "y":
                if value < price:
                    print(f"add {round(price - value, 2)} more to process:")
                    new_value = money_input()
                    value += new_value
                else:
                    money_sufficient = True
            else:
                money_sufficient = True
                print(f"Here is your refund of {value}$")
        if value > price:
            change = round(value - price, 2)
            print(f"Here is your {change}$ change")
            value = round(value - change, 2)
            subtract()
        elif value == price:
            subtract()
        print(f"Here is your {drink}. Enjoy!")









