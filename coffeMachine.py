MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 120.0,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 225.0,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 250.0,
    }
}

profit = 0

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def is_resources_sufficient(machine_resources,coffee_demand):
    """Checks whether resources required to make the product are sufficient or not"""
    is_resources = True
    for item in coffee_demand:
        if coffee_demand[item] >= machine_resources[item]:
            print(f"Sorry we ran don't have enough resources for {item}")
            is_resources = False
    return is_resources

def ask_payment(coffee):
    """Asks for money from the user"""

    print(f"Please insert money.\nYour bill : Rs.{coffee['cost']}")
    total = 0
    total += int(input("how many 200 rupee notes? ")) * 200
    total += int(input("how many 100 rupee notes? ")) * 100
    total += int(input("how many 50 rupee notes? ")) * 50
    total += int(input("how many 20 rupee notes? ")) * 20
    total += int(input("how many 10 rupee notes? ")) * 10
    return total

def is_transaction_successfull(payment,coffee_cost):
    """Checks whether the payment is sufficient or not"""
    if payment >= coffee_cost:
        change = payment - coffee_cost
        if change > 0:
            print(f"Money {change} returned.")
        global profit
        profit += coffee_cost
        return True
    else:
        print(f"insufficient payment! Rs.{round(payment,2)} is refunded.")
        return False

def make_coffee(coffee,drink_name):
    """Deducts main resources and updates the values"""
    for item in coffee:
        resources[item] -= coffee[item]
    print(f"Enjoy your {drink_name}!")
    

on = True
while on:
    choice = input("What would you like? (espresso/latte/cappuccino) ===>>> ").lower()
    if choice == "report":
        print(f"Water : {resources['water']} ml")
        print(f"Milk : {resources['milk']} ml")
        print(f"Coffee : {resources['coffee']} gms")
    elif choice == "off":
        print("Turning the machine off")
        on = False
    elif choice == "espresso" or choice == "latte" or choice == "cappuccino" :
        drink = MENU[choice]
        if is_resources_sufficient(resources,drink['ingredients']):
            payment = ask_payment(drink)
            if is_transaction_successfull(payment=payment,coffee_cost=drink["cost"]):
                make_coffee(coffee=drink["ingredients"],drink_name=choice)
    else:
        print("Enter a valid choice")