def move(cord):
    cords = cord.strip().split(" ")
    try:
        row = int(cords[0])
        col = int(cords[1])
    except:
        print("You typed wrong cords! Try again!")
        play()
        return
    try: 
        if game[row-1][col-1] == 0:
            game[row-1][col-1] = m
        else:
            print("This place is already taken choose another one!")
            play()
    except: 
        print("You choose cords outside the board! Try again!")
        play()

def play():
    cordX = input("What is your move(row col): ")
    move(cordX)

def end():
    for i in game:
        for j in i:
            if j == 0:
                return True
game = [[0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]]
i = 0
while end():
    if i % 2 == 0:
        m = 1
    else:
        m = 2
    if m == 1:
        print("Now is X move\n")
        play()
    elif m == 2:
        print("Now is O move\n")
        play()
    print(game)
    i += 1
print("\n  ---No more places---")