import pygame as pg
pg.init()

WIDTH,HEIGHT = 808,600
x,y = WIDTH-6, HEIGHT-50

screen = pg.display.set_mode([WIDTH,HEIGHT])

running = True
while running:

    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        
        screen.fill((255,255,255))
        pg.draw.line(screen,(0,0,255),(x/3+50,175),(x/3+50,2*y/3+175),3)
        pg.draw.line(screen,(0,0,255),(2*x/3-50,175),(2*x/3-50,2*y/3+175),3)
        pg.draw.line(screen,(0,0,255),(x/4,y/3+100),(3*x/4,y/3+100),3)
        pg.draw.line(screen,(0,0,255),(x/4,2*y/3+75),(3*x/4,2*y/3+75),3)
        pg.display.flip()
pg.quit()
