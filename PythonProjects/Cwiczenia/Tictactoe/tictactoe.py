#Tic Tac Toe Game
from os import system
global board
board = [' ' for x in range(10)]
global koniec 
koniec = True
def insert_letter(letter, pos):
    board[pos] = letter
def space_is_free(pos):
    return pos == ' '
def printboard(board):
    print(" "+ board[1]+' | '+board[2]+' | '+board[3])
    print('--- --- ---')
    print(" "+ board[4]+' | '+board[5]+' | '+board[6])
    print('--- --- ---')
    print(" "+ board[7]+' | '+board[8]+' | '+board[9])
    
def winner_on_board(b, l):
    return (b[7] == l and b[8] == l and b[9] == l) or (b[4] == l and b[5] == l and b[6] == l) or (b[1] == l and b[2] == l and b[3]== l) or (b[7] == l and b[4]== l and b[1]== l) or (b[8]==l and b[5]== l and b[2]== l) or (b[9]== l and b[6]== l and b[3]== l) or (b[9] == l and b[5]== l and b[1]==l)or (b[7]== l and b[5]== l and b[3]==l)
def player1_move(board):
    run = True
    while run:
        pole = input("Wybierz numer pola na którym chcesz postawic krzyzyk: ")
        pole = int(pole)
        if(space_is_free(board[pole])):
            insert_letter("X", pole)
            run = False
def player2_move(board):
    run = True
    while run:
        pole = input("Wybierz numer pola na którym chcesz postawic kolko: ")
        pole = int(pole)
        if(space_is_free(board[pole])):
            insert_letter('O', pole)
            run = False
    
def board_is_full(board):
    if not board.count(' ') > 1:
        return True
    else:
        return False
def main(board):
    gra = True
    print('Witam w grze w kolko i krzyzyk!')
    input('Kliknij enter, aby rozpocząć')
    while gra == True:
        
        
        
        while not (board_is_full(board)):
                system('cls')
                printboard(board)
                if not(winner_on_board(board, 'O')):
                    player1_move(board)
                    printboard(board)
                else:
                    print('Tym razem kolko wygralo!')
                    break
                system('cls')
                printboard(board)    
                if not(winner_on_board(board, 'X')):
                    player2_move(board)
                    printboard(board)
                else:
                    print('Tym razem krzyzyk wygral!')
                    break
                
        if board_is_full(board):
            print()
                     
        gra = input('Czy chcesz grac ponownie (t/n)')
        gra = gra.lower()
        global koniec
        print(gra)
        if(gra == 't' or koniec == 'tak'):
            koniec = True
        else:
            koniec = False

while(koniec):
    main(board)
    system('cls')
    board = [' ' for x in range(10)]