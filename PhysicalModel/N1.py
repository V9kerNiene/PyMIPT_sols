import graphics as gr
import math

szx = 1000
szy = 1000
G = 2000

window = gr.GraphWin("model", szx,szy)
coords = gr.Point(600,600)
velocity = gr.Point(1.5,-1.5)
acc = gr.Point(0,0)
ccl = gr.Circle(coords,10)
ccl.setFill('red')
ccl.draw(window)
def add(p1, p2):
    new_p = gr.Point(p1.x + p2.x, p1.y+p2.y)
    return new_p
def sub(p1, p2):
    new_p = gr.Point(p1.x - p2.x, p1.y-p2.y)
    return new_p
def drawc(coords):
    #circle = gr.Circle(coords,10)
    #circle.setFill('green')
    #circle.draw(window)
    sun = gr.Circle(gr.Point(400,400), 50)
    sun.setFill('yellow')
    sun.draw(window)
def cls():
    rct = gr.Rectangle(gr.Point(0,0), gr.Point(szx,szy))
    rct.draw(window)

def draw_ball(coords):
    circle = gr.Circle(coords,10)
    circle.setFill('red')
    circle.draw(window)

def check_coords(coords,velocity):
    if coords.x <0 or coords.x > szx:
        velocity.x = -velocity.x
    if coords.y < 0 or coords.y > szy:
        velocity.y = -velocity.y
def update_coords(coords,velocity):
    return add(coords,velocity)
def update_velocity(velocity,accel):
    return add(velocity,accel)
def update_acc(bcoords,ccoords):
    diff = sub(bcoords,ccoords)
    d2 = (diff.x**2 + diff.y**2)**(3/2)
    return gr.Point(-diff.x*G/d2, - diff.y*G/d2)


while True:
    cls()

    drawc(coords)
    acc = update_acc(coords, gr.Point(400,400))
    coords1 = update_coords(coords,velocity)
    s=sub(coords1, coords)
    ccl.move(s.x,s.y)
    coords = coords1
    velocity = update_velocity(velocity, acc)
    #check_coords(coords,velocity)
    gr.time.sleep(0.02)
