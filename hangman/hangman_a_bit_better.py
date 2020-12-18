import random

# Write your code here
print("H A N G M A N")

def game():
    guess_words = ['python', 'java', 'kotlin', 'javascript']
    aaa = 0
    random_word = random.choice(guess_words)
    split_random_word = list(random_word)

    random_word_length = len(random_word)

    # new_var = '-' * (random_word_length - 3)
    full_word = '-' * random_word_length
    lines_ept = list(full_word)

    # print(new)
    # print(split_random_word[1])
    # print(len(random_word))
    number = 0

    tries = 0
    # print('Guess the word ' + full_word + ': '):
    qqq = 0
    listik = []

    bad_words_list = []

    play = 0
    while True:
        if tries >= 8:
            print('You lost!')
            menu()
        elif qqq == 3:
            menu()
        elif play == 5:
            play = 0
        else:
            #                            ept))) nu vi ponyali
            print(''.join(map(str, lines_ept)))
            guess_word = input("Input a letter: ")
            if len(guess_word) == 1:
                if guess_word.islower():
                    if guess_word in random_word:
                        if guess_word not in listik:
                            bad_words_list.append(guess_word)
                            for char in range(len(split_random_word)):
                                if guess_word == split_random_word[char]:
                                    lines_ept[char] = guess_word
                                    listik.append(guess_word)
                                    print()
                                    if len(listik) == random_word_length:
                                        print(''.join(map(str, lines_ept)))
                                        print('You guessed the word!')
                                        print('You survived!')
                                        qqq = 3
                                        break

                        else:
                            print("You've already guessed this letter")
                            if tries >= 8:
                                print('You lost!')
                                menu()
                            print()
                    elif guess_word in bad_words_list:
                        print("You've already guessed this letter")
                        print()

                    else:
                        bad_words_list.append(guess_word)
                        tries = tries + 1
                        print("That letter doesn't appear in the word")
                        if tries >= 8:
                            print('You lost!')
                            menu()
                        print()
                else:

                    print('Please enter a lowercase English letter')
                    print()
            else:
                print('You should input a single letter')
                print()


def menu():
    while True:
        print()
        type_play_bro = input('Type "play" to play the game, "exit" to quit: ')
        if type_play_bro == 'exit':
            quit()
        elif type_play_bro == 'play':
            print()
            game()


if __name__ == '__main__':
    menu()

# print()
# print("Thanks for playing!"
#       "\nWe'll see how well you did in the next stage")