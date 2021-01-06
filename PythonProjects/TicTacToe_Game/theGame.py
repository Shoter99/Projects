def draw_board():
    print("""
     --- --- ---
    | %s | %s | %s |
     --- --- ---
    | %s | %s | %s |
     --- --- --- 
    | %s | %s | %s |
     --- --- ---   
     """ % (game[0][0],game[0][1],game[0][2],game[1][0],game[1][1],game[1][2],game[2][0],game[2][1],game[2][2]))

game = [[" ", " ", " "],
        [" ", " ", " "],
        [" ", " ", " "]]    
draw_board()