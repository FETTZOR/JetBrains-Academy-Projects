# write your code here
l = ['  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '  ']
axaxa = 0
print('---------\n'
      '|       |\n'
      '|       |\n'
      '|       |\n'
      '---------')
while True:
    count_x = 0

    count_o = 0


    def asd():
        d = ''.join(l[0:3])

        e = ''.join(l[3:6])

        f = ''.join(l[6:9])

        print('---------')
        print('| ' + d + '|')
        print('| ' + e + '|')
        print('| ' + f + '|')
        print('---------')


    x = 0
    o = 0

    if l[0] == 'O ' and l[1] == 'O ' and l[2] == 'O ' or l[3] == 'O ' and l[4] == 'O ' and \
            l[5] == 'O ':
        o = o + 1
    elif l[6] == 'O ' and l[7] == 'O ' and l[8] == 'O ' or l[0] == 'O ' and l[3] == 'O ' and \
            l[6] == 'O ':
        o = o + 1
    elif l[1] == 'O ' and l[4] == 'O ' and l[7] == 'O ' or l[2] == 'O ' and l[5] == 'O ' and \
            l[8] == 'O ':
        o = o + 1
    elif l[0] == 'O ' and l[4] == 'O ' and l[8] == 'O ' or l[2] == 'O ' and l[4] == 'O ' and \
            l[6] == 'O ':
        o = o + 1
    else:
        pass

    if l[0] == 'X ' and l[1] == 'X ' and l[2] == 'X ' or l[3] == 'X ' and l[4] == 'X ' and \
            l[5] == 'X ':
        x = x + 1
    elif l[6] == 'X ' and l[7] == 'X ' and l[8] == 'X ' or l[0] == 'X ' and l[3] == 'X ' and \
            l[6] == 'X ':
        x = x + 1
    elif l[1] == 'X ' and l[4] == 'X ' and l[7] == 'X ' or l[2] == 'X ' and l[5] == 'X ' and \
            l[8] == 'X ':
        x = x + 1
    elif l[0] == 'X ' and l[4] == 'X ' and l[8] == 'X ' or l[2] == 'X ' and l[4] == 'X ' and \
            l[6] == 'X ':
        x = x + 1
    else:
        pass
    print(x)
    print(l)
    if count_o - count_x == 0 or count_o - count_x == 1 or count_x - count_o == 0 or count_x - count_o == 1:
        if x == 1 and o == 1 and '  ' not in l:
            print('Draw')
            break

        elif x == 1 and o == 0:
            print('X wins')
            break

        elif x == 0 and o == 1:
            print('O wins')
            break

        elif x == 1 and o == 1:
            print('Impossible')
            break

        elif x == 0 and o == 0 and '  ' in l:

            while axaxa == 0:

                coordinates_input = input('Enter the coordinates: ')
                a, b = coordinates_input.split()

                try:

                    int(a)
                    int(b)

                    if a == '1' and b == '1' and l[6] == '  ':
                        l[6] = 'X '
                        asd()
                        axaxa = axaxa + 1
                        break
                    elif a == '2' and b == '1' and l[7] == '  ':
                        l[7] = 'X '
                        axaxa = axaxa + 1
                        asd()
                        break
                    elif a == '3' and b == '1' and l[8] == '  ':
                        l[8] = 'X '
                        asd()
                        axaxa = axaxa + 1
                        break
                    elif a == '1' and b == '2' and l[3] == '  ':
                        l[3] = 'X '
                        asd()
                        axaxa = axaxa + 1
                        break
                    elif a == '2' and b == '2' and l[4] == '  ':
                        l[4] = 'X '
                        asd()
                        axaxa = axaxa + 1
                        break
                    elif a == '3' and b == '2' and l[5] == '  ':
                        l[5] = 'X '
                        asd()
                        axaxa = axaxa + 1
                        break
                    elif a == '1' and b == '3' and l[0] == '  ':
                        l[0] = 'X '
                        asd()
                        axaxa = axaxa + 1
                        break
                    elif a == '2' and b == '3' and l[1] == '  ':
                        l[1] = 'X '
                        asd()
                        axaxa = axaxa + 1
                        break
                    elif a == '3' and b == '3' and l[2] == '  ':
                        l[2] = 'X '
                        asd()
                        axaxa = axaxa + 1
                        break

                    # occupied
                    elif a == '1' and b == '1' and l[6] != '  ' and count_x >= count_o:
                        print("This cell is occupied! Choose another one!")
                        axaxa = 0
                    elif a == '2' and b == '1' and l[7] != '  ' and count_x >= count_o:
                        print("This cell is occupied! Choose another one!")
                        axaxa = 0
                    elif a == '3' and b == '1' and l[8] != '  ' and count_x >= count_o:
                        print("This cell is occupied! Choose another one!")
                        axaxa = 0
                    elif a == '1' and b == '2' and l[3] != '  ' and count_x >= count_o:
                        print("This cell is occupied! Choose another one!")
                        axaxa = 0
                    elif a == '2' and b == '2' and l[4] != '  ' and count_x >= count_o:
                        print("This cell is occupied! Choose another one!")
                        axaxa = 0
                    elif a == '3' and b == '2' and l[5] != '  ' and count_x >= count_o:
                        print("This cell is occupied! Choose another one!")
                        axaxa = 0
                    elif a == '1' and b == '3' and l[0] != '  ' and count_x >= count_o:
                        print("This cell is occupied! Choose another one!")
                        axaxa = 0
                    elif a == '2' and b == '3' and l[1] != '  ' and count_x >= count_o:
                        print("This cell is occupied! Choose another one!")
                        axaxa = 0
                    elif a == '3' and b == '3' and l[2] != '  ' and count_x >= count_o:
                        print("This cell is occupied! Choose another one!")
                        axaxa = 0
                    elif a == '1' and b == '1' and l[6] != '  ' and count_o >= count_x:
                        print("This cell is occupied! Choose another one!")
                        axaxa = 0
                    elif a == '2' and b == '1' and l[7] != '  ' and count_o >= count_x:
                        print("This cell is occupied! Choose another one!")
                        axaxa = 0
                    elif a == '3' and b == '1' and l[8] != '  ' and count_o >= count_x:
                        print("This cell is occupied! Choose another one!")
                        axaxa = 0
                    elif a == '1' and b == '2' and l[3] != '  ' and count_o >= count_x:
                        print("This cell is occupied! Choose another one!")
                        axaxa = 0
                    elif a == '2' and b == '2' and l[4] != '  ' and count_o >= count_x:
                        print("This cell is occupied! Choose another one!")
                        axaxa = 0
                    elif a == '3' and b == '2' and l[5] != '  ' and count_o >= count_x:
                        print("This cell is occupied! Choose another one!")
                        axaxa = 0
                    elif a == '1' and b == '3' and l[0] != '  ' and count_o >= count_x:
                        print("This cell is occupied! Choose another one!")
                        axaxa = 0
                    elif a == '2' and b == '3' and l[1] != '  ' and count_o >= count_x:
                        print("This cell is occupied! Choose another one!")
                        axaxa = 0
                    elif a == '3' and b == '3' and l[2] != '  ' and count_o >= count_x:
                        print("This cell is occupied! Choose another one!")
                        axaxa = 0
                    else:
                        print("Coordinates should be from 1 to 3!")
                        axaxa = 0
                except:
                    print("You should enter numbers!")
                    axaxa = 0
        if l[0] == 'O ' and l[1] == 'O ' and l[2] == 'O ' or l[3] == 'O ' and l[4] == 'O ' and \
                l[5] == 'O ':
            o = 1
        elif l[6] == 'O ' and l[7] == 'O ' and l[8] == 'O ' or l[0] == 'O ' and l[3] == 'O ' and \
                l[6] == 'O ':
            o = 1
        elif l[1] == 'O ' and l[4] == 'O ' and l[7] == 'O ' or l[2] == 'O ' and l[5] == 'O ' and \
                l[8] == 'O ':
            o = 1
        elif l[0] == 'O ' and l[4] == 'O ' and l[8] == 'O ' or l[2] == 'O ' and l[4] == 'O ' and \
                l[6] == 'O ':
            o = 1
        else:
            pass

        if l[0] == 'X ' and l[1] == 'X ' and l[2] == 'X ' or l[3] == 'X ' and l[4] == 'X ' and \
                l[5] == 'X ':
            x = 1
        elif l[6] == 'X ' and l[7] == 'X ' and l[8] == 'X ' or l[0] == 'X ' and l[3] == 'X ' and \
                l[6] == 'X ':
            x = 1
        elif l[1] == 'X ' and l[4] == 'X ' and l[7] == 'X ' or l[2] == 'X ' and l[5] == 'X ' and \
                l[8] == 'X ':
            x = 1
        elif l[0] == 'X ' and l[4] == 'X ' and l[8] == 'X ' or l[2] == 'X ' and l[4] == 'X ' and \
                l[6] == 'X ':
            x = 1
        else:
            pass

        if x == 1 and o == 1 and '  ' not in l:
            print('Draw')
            break

        elif x == 1 and o == 0:
            print('X wins')
            break

        elif x == 0 and o == 1:
            print('O wins')
            break

        elif x == 1 and o == 1:
            print('Impossible')
            break

        elif x == 0 and o == 0 and '  ' in l:
            while axaxa == 1:
                player_o = input('Enter the coordinates sad: ')
                a, b = player_o.split()
                if axaxa != 0:
                    try:
                        int(a)
                        int(b)

                        if a == '1' and b == '1' and l[6] == '  ' and count_x >= count_o:
                            l[6] = 'O '
                            asd()
                            axaxa = 0
                            break
                        elif a == '2' and b == '1' and l[7] == '  ' and count_x >= count_o:
                            l[7] = 'O '
                            asd()
                            axaxa = 0
                            break
                        elif a == '3' and b == '1' and l[8] == '  ' and count_x >= count_o:
                            l[8] = 'O '
                            asd()
                            axaxa = 0
                            break
                        elif a == '1' and b == '2' and l[3] == '  ' and count_x >= count_o:
                            l[3] = 'O '
                            asd()
                            axaxa = 0
                            break
                        elif a == '2' and b == '2' and l[4] == '  ' and count_x >= count_o:
                            l[4] = 'O '
                            asd()
                            axaxa = 0
                            break
                        elif a == '3' and b == '2' and l[5] == '  ' and count_x >= count_o:
                            l[5] = 'O '
                            asd()
                            axaxa = 0
                            break
                        elif a == '1' and b == '3' and l[0] == '  ' and count_x >= count_o:
                            l[0] = 'O '
                            asd()
                            axaxa = 0
                            break
                        elif a == '2' and b == '3' and l[1] == '  ' and count_x >= count_o:
                            l[1] = 'O '
                            asd()
                            axaxa = 0
                            break
                        elif a == '3' and b == '3' and l[2] == '  ' and count_x >= count_o:
                            l[2] = 'O '
                            asd()
                            axaxa = 0
                            break
                        # occupied

                        elif a == '1' and b == '1' and l[6] != '  ' and count_x >= count_o:
                            print("This cell is occupied! Choose another one!")
                            axaxa = 1
                        elif a == '2' and b == '1' and l[7] != '  ' and count_x >= count_o:
                            print("This cell is occupied! Choose another one!")
                            axaxa = 1
                        elif a == '3' and b == '1' and l[8] != '  ' and count_x >= count_o:
                            print("This cell is occupied! Choose another one!")
                            axaxa = 1
                        elif a == '1' and b == '2' and l[3] != '  ' and count_x >= count_o:
                            print("This cell is occupied! Choose another one!")
                            axaxa = 1
                        elif a == '2' and b == '2' and l[4] != '  ' and count_x >= count_o:
                            print("This cell is occupied! Choose another one!")
                            axaxa = 1
                        elif a == '3' and b == '2' and l[5] != '  ' and count_x >= count_o:
                            print("This cell is occupied! Choose another one!")
                            axaxa = 1
                        elif a == '1' and b == '3' and l[0] != '  ' and count_x >= count_o:
                            print("This cell is occupied! Choose another one!")
                            axaxa = 1
                        elif a == '2' and b == '3' and l[1] != '  ' and count_x >= count_o:
                            print("This cell is occupied! Choose another one!")
                            axaxa = 1
                        elif a == '3' and b == '3' and l[2] != '  ' and count_x >= count_o:
                            print("This cell is occupied! Choose another one!")
                            axaxa = 1
                        elif a == '1' and b == '1' and l[6] != '  ' and count_o >= count_x:
                            print("This cell is occupied! Choose another one!")
                            axaxa = 1
                        elif a == '2' and b == '1' and l[7] != '  ' and count_o >= count_x:
                            print("This cell is occupied! Choose another one!")
                            axaxa = 1
                        elif a == '3' and b == '1' and l[8] != '  ' and count_o >= count_x:
                            print("This cell is occupied! Choose another one!")
                            axaxa = 1
                        elif a == '1' and b == '2' and l[3] != '  ' and count_o >= count_x:
                            print("This cell is occupied! Choose another one!")
                            axaxa = 1
                        elif a == '2' and b == '2' and l[4] != '  ' and count_o >= count_x:
                            print("This cell is occupied! Choose another one!")
                            axaxa = 1
                        elif a == '3' and b == '2' and l[5] != '  ' and count_o >= count_x:
                            print("This cell is occupied! Choose another one!")
                            axaxa = 1
                        elif a == '1' and b == '3' and l[0] != '  ' and count_o >= count_x:
                            print("This cell is occupied! Choose another one!")
                            axaxa = 1
                        elif a == '2' and b == '3' and l[1] != '  ' and count_o >= count_x:
                            print("This cell is occupied! Choose another one!")
                            axaxa = 1
                        elif a == '3' and b == '3' and l[2] != '  ' and count_o >= count_x:
                            print("This cell is occupied! Choose another one!")
                            axaxa = 1
                        else:
                            print("Coordinates should be from 1 to 3!")
                            axaxa = 1

                    except:
                        print("You should enter numbers!")
                        axaxa = 1
        else:
            print('Draw')
            break
    else:
        print('Impossible')
        break