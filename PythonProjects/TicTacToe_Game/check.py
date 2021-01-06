game = [[1, 2, 1],
          [1, 2, 0],
          [1, 2, 1]]


def check_if_win(list):
    x = 0
    o = 0
    for i in list:
        if i != 0:
            if i == 1:
                x += 1
            else:
                o += 1
    if x == 3:
        print("X won")
        exit()
    elif o == 3:
        print("o won")
        exit()


column = [[game[0][0], game[1][0], game[2][0]], [game[0][1],
                                                       game[1][1], game[2][1]], [game[0][2], game[1][2], game[2][2]]]
cross = [[game[0][0], game[1][1], game[2][2]],
         [game[0][2], game[1][1], game[2][0]]]
check_if_win(game[0])
check_if_win(game[1])
check_if_win(game[2])
check_if_win(column[0])
check_if_win(column[1])
check_if_win(column[2])
check_if_win(cross[0])
check_if_win(cross[1])
