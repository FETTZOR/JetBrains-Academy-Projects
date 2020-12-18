def water_at_the_moment():
    water = 400
    print('The coffee machine has:')
    print(f'{water} of water')
    return water


def milk_at_the_moment():
    milk = 540
    print(f'{milk} of milk')
    return milk


def beans_at_the_moment():
    coffee_beans = 120
    print(f'{coffee_beans} of coffee beans')
    return coffee_beans


def cups_at_the_moment():
    disposable_cups = 9
    print(f'{disposable_cups} of disposable cups')
    return disposable_cups


def money_at_the_moment():
    money = 550
    print(f'{money} of money')
    return money


def write_action():
    print('Write action (buy, fill, take, remaining, exit):')
    action = input()
    return action


def buy():
    print('What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:')
    choose_coffee = input()
    return choose_coffee


def milk_after_cappuccino(milk_cap):
    milk = milk_cap - 100
    return milk


def beans_after_cappuccino(beans_cap):
    beans = beans_cap - 12
    return beans


def cups_after(cups):
    cups = cups - 1
    return cups


def money_after_cappuccino(money_cap):
    money = money_cap + 6
    return money


# latte
def water_after_latte(water_lat):
    water = water_lat - 350
    return water


def milk_after_latte(milk_lat):
    milk = milk_lat - 75
    return milk


def beans_after_latte(beans_lat):
    beans = beans_lat - 20
    return beans


def money_after_latte(money_lat):
    money = money_lat + 7
    return money


# espresso
def water_after_espresso(water_esp):
    water = water_esp - 250
    return water


def milk_after_espresso(milk_esp):
    milk = milk_esp - 0
    return milk


def beans_after_espresso(beans_esp):
    beans = beans_esp - 16
    return beans


def money_after_espresso(money_esp):
    money = money_esp + 4
    return money


# fill
def water_add(water_fill):
    print('Write how many ml of water do you want to add:')
    water_add_input = int(input())
    water_fill = water_fill + water_add_input
    return water_fill


def milk_add(milk_fill):
    print('Write how many ml of milk do you want to add:')
    milk_add_input = int(input())
    milk_fill = milk_fill + milk_add_input
    return milk_fill


def beans_add(beans_fill):
    print('Write how many grams of coffee beans do you want to add:')
    beans_add_input = int(input())
    beans_fill = beans_fill + beans_add_input
    return beans_fill


def cups_add(cups_fill):
    print('Write how many disposable cups of coffee do you want to add:')
    cups_add_input = int(input())
    cups_fill = cups_fill + cups_add_input
    return cups_fill


def money_take(money_take_away):
    money_take_away = money_take_away - money_take_away
    return money_take_away
