import turtle as t
import random as rand
t.hideturtle()

t.screensize(640, 480)
posx = 1
posy = 1
p1 = 0.3333
p2 = 0.6666
p3 = 1


for i in range(0, 100):
    t.penup()
    t.setpos(posx, posy)
    t.pendown()
    t.dot()
    los = rand.random()
    print(los)
    if los < p1:
        posx = ((posx*0.5)-0.5)*100
        posy = ((posy*0.5)+0.5)*100
        print(posx, posy)
    elif los < p2 and los > p1:
        posx = ((posx*0.5)-0.5)*100
        posy = ((posy*0.5)-0.5)*100
        print(posx, posy)
    elif los < p3 and los > p2:
        posx = ((posx*0.5)+0.5)*100
        posy = ((posy*0.5)-0.5)*100
        print(posx, posy)
t.exitonclick()
