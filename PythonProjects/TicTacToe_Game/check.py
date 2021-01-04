matrix = [[1, 2, 1],
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


column = [[matrix[0][0], matrix[1][0], matrix[2][0]], [matrix[0][1],
                                                       matrix[1][1], matrix[2][1]], [matrix[0][2], matrix[1][2], matrix[2][2]]]
cross = [[matrix[0][0], matrix[1][1], matrix[2][2]],
         [matrix[0][2], matrix[1][1], matrix[2][0]]]
check_if_win(matrix[0])
check_if_win(matrix[1])
check_if_win(matrix[2])
check_if_win(column[0])
check_if_win(column[1])
check_if_win(column[2])
check_if_win(cross[0])
check_if_win(cross[1])
