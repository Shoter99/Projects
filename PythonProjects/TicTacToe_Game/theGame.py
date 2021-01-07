def draw_board(): #Function that draws a board
    print("""
     --- --- ---
    | %s | %s | %s |
     --- --- ---
    | %s | %s | %s |
     --- --- --- 
    | %s | %s | %s |
     --- --- ---   
     """ % (game[0][0],game[0][1],game[0][2],game[1][0],game[1][1],game[1][2],game[2][0],game[2][1],game[2][2]))
def check_if_win(list): #Check if X or O won game in one line
    x = 0
    o = 0
    global game_end
    for i in list:
        if i != " ":
            if i == "X":
                x += 1
            elif i == "O":
                o += 1
    if x == 3:
        print("X won")
        gamefinish = input("Do you want to start again? ")
        if gamefinish.lower() != "yes":
            exit()
        else:
            print("\n New Game \n")
            game_end = True
    elif o == 3:
        print("o won")
        gamefinish = input("Do you want to start again? ")
        if gamefinish.lower() != "yes":
            exit()
        else:
            print("\n New Game \n")
            game_end = True
def check(): #Checks every line for winner
        check_if_win(game[0])
        check_if_win(game[1])
        check_if_win(game[2])
        check_if_win(column[0])
        check_if_win(column[1])
        check_if_win(column[2])
        check_if_win(cross[0])
        check_if_win(cross[1])

def move(cord): # Move player
    cords = cord.strip().split(" ")
    try:
        row = int(cords[0])
        col = int(cords[1])
    except:
        print("You typed wrong cords! Try again!")
        play()
        return
    try: 
        if game[row-1][col-1] == " ":
            game[row-1][col-1] = m
        else:
            print("This place is already taken choose another one!")
            play()
    except: 
        print("You choose cords outside the board! Try again!")
        play()

def play(): # Ask player for move
    cordX = input("What is your move(row col): ")
    move(cordX)

def end(): # Checks if game has ended
    for i in game:
        for j in i:
            if j == " ":
                return True

game_end = False
game = [[" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "]] 
i = 0
while end():
        draw_board()
        column = [[game[0][0], game[1][0], game[2][0]], [game[0][1],
                                                        game[1][1], game[2][1]], [game[0][2], game[1][2], game[2][2]]]
        cross = [[game[0][0], game[1][1], game[2][2]],
            [game[0][2], game[1][1], game[2][0]]]  
        if i % 2 == 0:
            m = "X"
        else:
            m = "O"
        
        if m == "X":
            check()
            if game_end == True:
                game = [[" ", " ", " "],
                        [" ", " ", " "],
                        [" ", " ", " "]] 
                i = 0
                game_end = False
                continue
            print("Now is X move\n")
            play()
        elif m == "O":
            check()
            if game_end == True:
                game = [[" ", " ", " "],
                        [" ", " ", " "],
                        [" ", " ", " "]] 
                i = 0
                game_end = False
                continue
            print("Now is O move\n")
            play()
        i += 1
    
print("\n  ---No more places---")