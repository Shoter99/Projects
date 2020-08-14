import math
import pygame as pg
import random
import os
#display setup
pg.init()
WIDTH, HEIGHT = 800, 500
win = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("Hangman Game!")
#load images
images = []
for i in range(7):
    try:
        mydir = os.path.dirname(__file__)
        image = pg.image.load(os.path.join(mydir,r'data\hangman%d.png' % i))
        images.append(image)
    except :
        print('Nie udało się załadować obrazków')
print (images)
#font
LETTER_FONT = pg.font.SysFont('Times New Roman', 24)
WORD_FONT = pg.font.SysFont('comic_sans', 36)
#game variables
hangman_status = 0
guessed = []
password = ['REKIN', 'KOMPUTER', 'KRZESŁO', 'SŁOWNIK', 'KACZKA', 'APARAT', 'TELEFON', 'SZKOŁA', 'PIES']
num = random.randint(0,8)
word = password[num]
#colors
WHITE = (255,255,255)
BLACK = (0,0,0)


#game loop
FPS = 60
clock = pg.time.Clock()
run = True

#button variables
RADIUS = 25
GAP = 15
letters = []
startx = round((WIDTH - (RADIUS * 2 + GAP)*12)/2)
starty = 300
def drawbutton():
    let = ['A','Ą','B','C','Ć','D','E','Ę','F','G','H','I','J','K','L','Ł','M','N','Ń','O','Ó','P','Q','R','S','Ś','T','U','V','W','X','Y','Z','Ź','Ż']
    for i in range(35):
        x = startx + GAP * 2 + ((RADIUS * 2 + GAP) * (i % 12))
        y = starty + ((i // 12) * (GAP + RADIUS * 2))
        letters.append([x, y, let[i], True])

def draw():
    win.fill(WHITE)

    #draw word 
    display_word = ""
    for letter in word:
        if letter in guessed:
            display_word += letter + " "
        else:
            display_word += "_ "
        text = WORD_FONT.render(display_word,1,BLACK)
        win.blit(text,(400,100))


    #draw buttons 
    for letter in letters:
        x, y, ltr, visible = letter
        if visible:
            pg.draw.circle(win, BLACK, (x,y), RADIUS, 3)
            text = WORD_FONT.render(ltr, 1, BLACK)
            win.blit(text, ((int(x - text.get_width()/2), int(y - text.get_height()/2))))

    win.blit(images[hangman_status], (100, 50))
    pg.display.update()
drawbutton()
#funkcja
def write_messege(message):
        win.fill(WHITE)
        text = LETTER_FONT.render(message, 1, BLACK)
        win.blit(text, (int(WIDTH/2 - text.get_width()/2), int(HEIGHT/2 - text.get_height()/2 )))
        pg.display.update()



while run:
        
        clock.tick(FPS)

        draw()
        

        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False
            if event.type == pg.MOUSEBUTTONDOWN:
                m_x, m_y = pg.mouse.get_pos()
                for letter in letters:
                    x, y, ltr, visible = letter
                    if visible:
                        dis = math.sqrt((x - m_x)**2 +(y-m_y)**2)
                        if dis < RADIUS:
                            letter[3] = False
                            guessed.append(ltr)
                            if ltr not in word:
                                hangman_status += 1
                                print(hangman_status)
        won = True
        for letter in word:
            if letter not in guessed:
                won = False
                break
        if won:
            write_messege("Udało ci się, wygrałeś")
            pg.time.delay(3000)
            guessed = []
            hangman_status = 0
            num = random.randint(0,8)
            word = password[num]
            won = True
            win.fill(WHITE)
            letters.clear()
            drawbutton()
            
        if hangman_status == 6:
            write_messege("Niestety tym razem Ci się nie udało. Hasłem było: %s" % word)
            pg.time.delay(3000)
            guessed = []
            hangman_status = 0
            num = random.randint(0,8)
            word = password[num]
            won = True
            win.fill(WHITE)
            letters.clear()
            drawbutton()
            
            

pg.quit()