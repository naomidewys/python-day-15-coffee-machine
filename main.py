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

# Set coffee machine standards
machine_on = True
money = 0

# Checks whether there is enough ingredients to make the chosen drink
def is_resource_sufficient(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"Sorry, the machine is out of {item}. Please try another option.")
            return False
        else:
            return True

# Calculates the coins entered by the user
def process_coins():
    quarter = float(input("How many quarters (25c)? "))
    dime = float(input("How many dimes (10c)? "))
    nickel = float(input("How many nickels (5c)? "))
    penny = float(input("How many pennies (1c)? "))
    total_money = (quarter * 0.25) + (dime * 0.1) + (nickel * 0.05) + (penny * 0.01)
    return total_money

# Checks whether payment covers the drink, returns change if money received is greater than cost
def is_transaction_successful(money_received, drink_cost):
    global money
    if money_received == drink_cost:
        money += money_received
        return True
    elif money_received > drink_cost:
        change = abs(round(drink_cost - money_received, 2))
        print(f"Here is your change: ${change}")
        money += drink_cost
        return True
    else:
        print("Sorry, you have insufficient funds. Money refunded.")
        return False

# Deducts ingredients from the available resources
def make_coffee(drink_name, order_ingredients):
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Enjoy your {drink_name}!")

# loops through drink orders while resources are available and machine is on
while machine_on:
    print("""
 ____        _   _                    ____       __  __           
|  _ \ _   _| |_| |__   ___  _ __    / ___|___  / _|/ _| ___  ___ 
| |_) | | | | __| '_ \ / _ \| '_ \  | |   / _ \| |_| |_ / _ \/ _ |
|  __/| |_| | |_| | | | (_) | | | | | |__| (_) |  _|  _|  __/  __/
|_|    \__, |\__|_| |_|\___/|_| |_|  \____\___/|_| |_|  \___|\___|
       |___/                                                      
          """)
    coffee_order = input("What would you like? (espresso, latte, cappuccino): ").lower()

    # turns off machine
    if coffee_order == "off":
        machine_on = False
    # provides report on current resource quantities and total profit made
    elif coffee_order == "report":
        print(f"Water: {resources["water"]}ml")
        print(f"Milk: {resources["milk"]}ml")
        print(f"Coffee: {resources["coffee"]}g")
        print(f"Money: ${money}")
    # runs drink order
    else:
        drink = MENU[coffee_order]
        if is_resource_sufficient(drink["ingredients"]):
            if is_transaction_successful(process_coins(), drink["cost"]):
                make_coffee(coffee_order, drink["ingredients"])
    

    

