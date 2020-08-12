liczba = 50
wm = ''
run = True
win = 'nie'
lastGuess = ''
print('Witaj w grze, wybierz liczbe od 1 do 100, a ja sprobuje ja zgadnac ')
def ask(liczba, wm, win): 
        print('Czy twoja liczba to %d ?' % (liczba))
        win = input('(tak, nie): ')
        if (win == 'nie'):
                wm = input('Wiecej czy mniej? ')
        if (win == 'tak'):
                run = False
while run == True:
    ask(liczba, wm, win)
    while(win == 'nie'):
        if (wm != ''):
            if (wm == 'mniej'):
                    liczba/2
                    wm = lastGuess
                    ask(liczba, wm, win)
                    while (wm == lastGuess):
                        liczba - 10
                        ask()
                        wm = lastGuess
                    while (wm != lastGuess):
                        liczba + 1
                        ask(liczba,wm, win)            
            elif (wm == 'wiecej'):
                liczba + 25
                wm = lastGuess
                ask(liczba,wm, win)
                while (wm == lastGuess):
                    liczba + 10
                    ask(liczba,wm, win)
                    wm = lastGuess
                while (wm != lastGuess):
                    liczba - 1
                    ask(liczba,wm, win)
                    wm = lastGuess
    run = False

            




