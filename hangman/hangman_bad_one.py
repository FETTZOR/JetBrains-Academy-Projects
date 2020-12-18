import random
# Write your code here
print("H A N G M A N")
print()
guess_words = ['python', 'java', 'kotlin', 'javascript']
aaa = 0
random_word = random.choice(guess_words)
split_random_word = list(random_word)

random_word_length = len(random_word)
random_word_length2 = len(random_word)

# new_var = '-' * (random_word_length - 3)
full_word = '-' * random_word_length
new = list(full_word)

# print(new)
# print(split_random_word[1])
# print(len(random_word))
number = 0

tries = 0
# print('Guess the word ' + full_word + ': ')

listik = []
while tries < 9:
    print(''.join(map(str, new)))
    guess_word = input("Input a letter: ")
    if guess_word in split_random_word:
        if guess_word not in listik:
            aaa = split_random_word.index(guess_word)
            listik.append(guess_word)
            # if len(listik) >= 2:
            #     if listik[-1] != [-2]:
            #         number = number + 1
            #     elif listik[-1] == [-2]:
            #         tries = tries + 1
            # print(aaa)
            # print(new)
            number = number + 1
            new.insert(aaa, guess_word)
            new.pop(aaa+1)
            # print(new)
            tries = tries + 1
            if guess_word == 'a':
                new.insert(3, guess_word)
                new.pop(4)
                number = number + 1
            if tries == 8:
                print()
                print('Thanks for playing!')
                print("We'll see how well you did in the next stage")
                break
            print()
            # if number == random_word_length:
            #     print()
            #     print('Thanks for playing!')
            #     print("We'll see how well you did in the next stage")
            #     break
        else:
            print()
            tries = tries + 1
            if tries == 8:
                print()
                print('Thanks for playing!')
                print("We'll see how well you did in the next stage")
                break
        # bbb = aaa - 1
        # insert_remove = new.pop(bbb)
    else:
        print("That letter doesn't appear in the word")
        print()
        tries = tries + 1
        if tries == 8:
            print()
            print('Thanks for playing!')
            print("We'll see how well you did in the next stage")
            break