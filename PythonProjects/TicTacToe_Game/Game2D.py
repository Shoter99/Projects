import pygame as pg
pg.init()

WIDTH,HEIGHT = 808,700

screen = pg.display.set_mode([WIDTH,HEIGHT])

running = True
while running:

    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        
        screen.fill((255,255,255))
        pg.draw.line(screen,(0,0,255),(WIDTH/3,0),(WIDTH/3,HEIGHT),2)
        pg.display.flip()
pg.quit()
