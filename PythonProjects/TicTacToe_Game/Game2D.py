import pygame as pg
pg.init()

#draws Gameboard
def Gameboard():       
    screen.fill((255,255,255))
    #board
    draw.rect(screen,(BLUE),(x/4,175,x/2,2*y/3),3)
    #columns
    draw.line(screen,(BLUE),(x/3+r,175),(x/3+r,2*y/3+175),3) 
    draw.line(screen,(BLUE),(2*x/3-r,175),(2*x/3-r,2*y/3+175),3)
    #rows
    draw.line(screen,(BLUE),(x/4,y/3+100+z),(3*x/4,y/3+100+z),3)
    draw.line(screen,(BLUE),(x/4,2*y/3+75-z),(3*x/4,2*y/3+75-z),3)

#SCREEN width and height
WIDTH,HEIGHT = 808,600
#Colors
BLUE = 0,0,255


x,y = WIDTH-6, HEIGHT-50
r,z = 65,15

screen = pg.display.set_mode([WIDTH,HEIGHT])
pg.display.set_caption("Tic Tac Toe Game")
font = pg.font.Font('PottaOne-Regular.ttf',32)
text = font.render('Now is O turn',True,BLUE)
draw = pg.draw
running = True


while running:

    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        screen.blit(text,(50,200))
        Gameboard()
        pg.display.flip()
        pg.display.update()
pg.quit()
