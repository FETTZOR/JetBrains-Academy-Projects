import random


# Write your code here
class BankingSystem:
    user_card_number_created = []
    user_card_number_log_in = []
    user_pin = []
    log_in_input = ""
    user_input = ""
    card_and_pin = {}

    log_in_card = []
    log_in_pin = []

    def __init__(self):
        print("1.  Create an account\n2. Log into account\n0. Exit")
        BankingSystem.account_create_login(self)

    def account_create_login(self):
        self.user_input = input()
        BankingSystem.user_account(self)

    def user_account(self):
        if self.user_input == '1':
            BankingSystem.create_card_number(self)
        if self.user_input == '2':
            BankingSystem.log_in(self)
        if self.user_input == '0':
            print("Bye!")
            quit()

    def create_card_number(self):
        # 6
        BankingSystem.user_card_number_created = [4, 0, 0, 0, 0, 0]

        # 7-16
        BankingSystem.user_card_number_created.append(random.randint(0, 9))
        BankingSystem.user_card_number_created.append(random.randint(0, 9))
        BankingSystem.user_card_number_created.append(random.randint(0, 9))
        BankingSystem.user_card_number_created.append(random.randint(0, 9))
        BankingSystem.user_card_number_created.append(random.randint(0, 9))
        BankingSystem.user_card_number_created.append(random.randint(0, 9))
        BankingSystem.user_card_number_created.append(random.randint(0, 9))
        BankingSystem.user_card_number_created.append(random.randint(0, 9))
        BankingSystem.user_card_number_created.append(random.randint(0, 9))
        BankingSystem.user_card_number_created.append(random.randint(0, 9))

        print("\nYour card has been created")
        print("Your card number:")
        print(''.join(map(str, BankingSystem.user_card_number_created)))

        self.card_num_to_dict = ''.join(map(str, BankingSystem.user_card_number_created))

        BankingSystem.create_pin(self)

    def create_pin(self):
        BankingSystem.user_pin = []
        BankingSystem.user_pin.append(random.randint(0, 9))
        BankingSystem.user_pin.append(random.randint(0, 9))
        BankingSystem.user_pin.append(random.randint(0, 9))
        BankingSystem.user_pin.append(random.randint(0, 9))

        print("Your card PIN:")
        print(''.join(map(str, BankingSystem.user_pin)))
        self.card_pin_to_dict = ''.join(map(str, BankingSystem.user_pin))
        print()

        BankingSystem.put_info_in_dictionary(self)

    def put_info_in_dictionary(self):

        BankingSystem.card_and_pin[self.card_num_to_dict] = self.card_pin_to_dict
        print(BankingSystem.card_and_pin)
        BankingSystem.__init__(self)

    def log_in(self):
        print("Enter your card number:")
        log_in_input = input()
        BankingSystem.log_in_card = list(log_in_input)

        print("Enter your PIN")
        pin_input = input()
        BankingSystem.log_in_pin = pin_input
        if log_in_input in self.card_and_pin:
            keys_list = list(self.card_and_pin)
            values_list = list(self.card_and_pin.values())
            key_index = list(self.card_and_pin.keys()).index(log_in_input)
            key = keys_list[key_index]
            value = values_list[key_index]
            if key in log_in_input and value in pin_input:
                print("\nYou have successfully logged in!\n")
                BankingSystem.account_management(self)
            else:
                print("\nWrong card number or PIN!\n")
                BankingSystem.__init__(self)

        else:
            print("\nWrong card number or PIN!\n")
            BankingSystem.__init__(self)

    def account_management(self):
        print("1. Balance\n2. Log out\n0. Exit")
        choose_palvelu = input()
        if choose_palvelu == "1":
            print("Balance: 0")
            self.account_management()
        elif choose_palvelu == "2":
            BankingSystem.__init__(self)
        elif choose_palvelu == "0":
            print("Bye!")
            quit()


if __name__ == '__main__':
    b_s = BankingSystem()