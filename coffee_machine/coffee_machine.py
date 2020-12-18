# Write your code here
import stage_four as fo


def main():
    water_at = 400
    milk_at = 540
    beans_at = 120
    cups_at = 9
    money_at = 550

    water_cap = 200
    milk_cap = 100
    beans_cap = 12
    money_cap = 6

    single_cup = 1

    water_lat = 350
    milk_lat = 75
    beans_lat = 20
    money_lat = 7

    water_esp = 250
    milk_esp = 0
    beans_esp = 16
    money_esp = 4
    while True:
        action = fo.write_action()
        print()
        if action == 'buy':
            buy = fo.buy()
            # cappuccino
            if buy == '3':
                if water_at >= water_cap and milk_at >= milk_cap and beans_at >= beans_cap and cups_at >= single_cup:
                    print('I have enough resources, making you a coffee!')
                    print()
                    water_at = water_at - water_cap
                    milk_at = milk_at - milk_cap
                    beans_at = beans_at - beans_cap
                    money_at = money_at + money_cap
                    cups_at = cups_at - single_cup
                elif water_at < water_cap:
                    print('Sorry, not enough water!')
                    print()
                elif milk_at < milk_cap:
                    print('Sorry, not enough milk!')
                    print()
                elif beans_at < beans_cap:
                    print('Sorry, not enough coffee beans!')
                    print()
                elif cups_at < single_cup:
                    print('Sorry, not enough disposable cups!')
                    print()
            # latte
            elif buy == '2':
                if water_at >= water_lat and milk_at >= milk_lat and beans_at >= beans_lat and cups_at >= single_cup:
                    print('I have enough resources, making you a coffee!')
                    print()
                    water_at = water_at - water_lat
                    milk_at = milk_at - milk_lat
                    beans_at = beans_at - beans_lat
                    money_at = money_at + money_lat
                    cups_at = cups_at - single_cup
                elif water_at < water_lat:
                    print('Sorry, not enough water!')
                    print()
                elif milk_at < milk_lat:
                    print('Sorry, not enough milk!')
                    print()
                elif beans_at < beans_lat:
                    print('Sorry, not enough coffee beans!')
                    print()
                elif cups_at < single_cup:
                    print('Sorry, not enough disposable cups!')
                    print()

            elif buy == '1':
                if water_at >= water_esp and milk_at >= milk_esp and beans_at >= beans_esp and cups_at >= single_cup:
                    print('I have enough resources, making you a coffee!')
                    print()
                    water_at = water_at - water_esp
                    milk_at = milk_at - milk_esp
                    beans_at = beans_at - beans_esp
                    money_at = money_at + money_esp
                    cups_at = cups_at - single_cup

                elif water_at < water_esp:
                    print('Sorry, not enough water!')
                    print()
                elif milk_at < milk_esp:
                    print('Sorry, not enough milk!')
                    print()
                elif beans_at < beans_esp:
                    print('Sorry, not enough coffee beans!')
                    print()
                elif cups_at < single_cup:
                    print('Sorry, not enough disposable cups!')
                    print()

            elif buy == 'back':
                pass

        elif action == 'fill':
            water_at = water_at + int(input('Write how many ml of water do you want to add:\n'))
            milk_at = milk_at + int(input('Write how many ml of milk do you want to add:\n'))
            beans_at = beans_at + int(input('Write how many grams of coffee beans do you want to add:\n'))
            cups_at = cups_at + int(input('Write how many disposable cups of coffee do you want to add:\n'))
            print()
        elif action == 'take':
            print(f'I gave you ${money_at}')
            money_at = money_at - money_at
            print()
        elif action == 'remaining':
            print('The coffee machine has:\n'
                  f'{water_at} of water\n'
                  f'{milk_at} of milk\n'
                  f'{beans_at} of coffee beans\n'
                  f'{cups_at} of disposable cups\n'
                  f'${money_at} of money')
            print()
        elif action == 'exit':
            break


if __name__ == '__main__':
    main()
