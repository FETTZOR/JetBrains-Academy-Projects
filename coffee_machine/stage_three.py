# fun1 coffee machine
def ask_user_water_ml():
    print('Write how many ml of water the coffee machine has:')
    water_ml = int(input())
    return water_ml


def ask_user_milk_ml():
    print('Write how many ml of milk the coffee machine has:')
    milk_has = int(input())
    return milk_has


def ask_user_beans():
    print('Write how many grams of coffee beans the coffee machine has:')
    beans_has = int(input())
    return beans_has


def ask_user_cups():
    print('Write how many cups of coffee you will need:')
    cups_need = int(input())
    return cups_need


def calc(a, b):
    return a // b


def calc_expected(a, b):
    return a - b


def calc_how_many_could_make(actual_cups_water, actual_cups_milk, actual_cups_beans):
    return min(actual_cups_water, actual_cups_milk, actual_cups_beans)


def print_result(possibility, cups_need, expected):
    if possibility < cups_need:
        print(f'No, I can make only {possibility} cups of coffee')

    elif possibility == cups_need:
        print('Yes, I can make that amount of coffee')

    elif possibility > cups_need:
        print(f'Yes, I can make that amount of coffee (and even {expected} more than that)')
