import math
import pygame
#display setup
pygame.init()
WIDTH, HEIGHT = 800, 500
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Hangman Game!")
#load images
images = []
for i in range(7):
    image = pygame.image.load('hangman%d.png' % i)
    images.append(image)
print (images)
#game variables
hangman_status = 0
#colors
WHITE = (255,255,255)
BLACK = (0,0,0)
#game loop
FPS = 60
clock = pygame.time.Clock()
run = True
#font
LETTER_FONT = pygame.font.SysFont('Times New Roman', 32)
#button variables
RADIUS = 25
GAP = 15
letters = []
startx = round((WIDTH - (RADIUS * 2 + GAP)*12)/2)
starty = 300

let = ['A','Ą','B','C','Ć','D','E','Ę','F','G','H','I','J','K','L','Ł','M','N','Ń','O','Ó','P','Q','R','S','Ś','T','U','W','X','Y','Z','Ź','Ż']
for i in range(34):
    x = startx + GAP * 2 + ((RADIUS * 2 + GAP) * (i % 12))
    y = starty + ((i // 12) * (GAP + RADIUS * 2))
    letters.append([x, y, let[i], True])

def draw():
    win.fill(WHITE)

    #draw buttons 
    for letter in letters:
        x, y, ltr, visible = letter
        if visible:
            pygame.draw.circle(win, BLACK, (x,y), RADIUS, 3)
            text = LETTER_FONT.render(ltr, 1, BLACK)
            win.blit(text, (x - text.get_width()/2, y - text.get_height()/2))

    win.blit(images[hangman_status], (100, 50))
    pygame.display.update()
while run:
    clock.tick(FPS)

    draw()
    

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            m_x, m_y = pygame.mouse.get_pos()
            for letter in letters:
                x, y, ltr, visible = letter
                if visible:
                    dis = math.sqrt((x - m_x)**2 +(y-m_y)**2)
                    if dis < RADIUS:
                        letter[3] = False


pygame.quit()