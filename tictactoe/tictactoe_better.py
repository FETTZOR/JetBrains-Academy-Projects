toe_desk = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
toe_symbols = ['X', 'O']


def print_desk():
    print("---------")
    for idk in range(0, 3):
        print("|", toe_desk[idk][0], toe_desk[idk][1], toe_desk[idk][2], "|")
    print("---------")


def game():
    start = 0
    end_gam = False
    while not end_gam:
        move = False
        while not move:
            input_coordinates = input("Enter the coordinates: ")
            coord_list = []
            for ii in input_coordinates:
                if ii.isnumeric():
                    coord_list.append(int(ii))
                    continue
                elif ii.isspace():
                    continue
                else:
                    print("You should enter numbers!")
                    coord_list.clear()
                    break
            if len(coord_list) > 1:
                if (coord_list[0] > 3) or (coord_list[0] < 1) or (coord_list[1] > 3) or (coord_list[1] < 1):
                    print("Coordinates should be from 1 to 3")
                elif toe_desk[abs(coord_list[1] - 3)][coord_list[0] - 1] != " ":
                    print("This cell is occupied! Choose another one!")
                else:
                    toe_desk[abs(coord_list[1] - 3)][coord_list[0] - 1] = toe_symbols[start]
                    move = True
                    start = (start + 1) % 2
                    print_desk()
                    end_gam = toe_desk_creation()


def toe_desk_creation():
    X = False
    O = False
    EMPTY = False
    x_totally = 0
    o_total = 0
    new = 2
    x_hor = 0
    x_hor_count = 0
    o_hor = 0
    o_hor_count = 0
    aaa = 0
    for i in range(0, 3):
        x_vert = 0
        o_vert = 0
        x_vert_count = 0
        o_vert_count = 0
        if toe_desk[i][aaa] == "X":
            x_hor += 1

        if toe_desk[i][aaa] == "O":
            o_hor += 1

        if toe_desk[new][i] == "X":
            x_hor_count += 1

        if toe_desk[new][i] == "O":
            o_hor_count += 1

        aaa += 1
        new -= 1
        for y in range(0, 3):
            if toe_desk[i][y] == " ":
                EMPTY = True
            if toe_desk[i][y] == "X":
                x_vert += 1
                x_totally += 1
            if toe_desk[i][y] == "O":
                o_vert += 1
                o_total += 1
            if toe_desk[y][i] == "O":
                o_vert_count += 1
            if toe_desk[y][i] == "X":
                x_vert_count += 1
        if (x_vert == 3) | (x_vert_count == 3) | (x_hor == 3) | (x_hor_count == 3):
            X = True
        if (o_vert == 3) | (o_vert_count == 3) | (o_hor == 3) | (o_hor_count == 3):
            O = True
    if X:
        print("X wins")
        return True
    elif O:
        print("O wins")
        return True
    elif not EMPTY:
        print("Draw")
        return True
    else:
        return False


print_desk()
game()
