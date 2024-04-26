import graphics as gr
import math

szx = 1000
szy = 1000
G = 2000

window = gr.GraphWin("model", szx,szy)
pi = 3.1415926535
def cls():
    rct = gr.Rectangle(gr.Point(0,0), gr.Point(szx,szy))
    rct.setFill('white')
    rct.draw(window)
coords = gr.Point(600,300)
ccl = gr.Circle(coords,10)
ccl.setFill('red')
ccl.draw(window)
l=100
def update_coords(coords,velocity):
    return add(coords,velocity)
def update_velocity(velocity,accel):
    return add(velocity,accel)
def update_acc(bcoords,ccoords):
    diff = sub(bcoords,ccoords)
    d2 = (diff.x**2 + diff.y**2)**(3/2)
    return gr.Point(-diff.x*G/d2, - diff.y*G/d2)
def add(p1, p2):
    new_p = gr.Point(p1.x + p2.x, p1.y+p2.y)
    return new_p
def sub(p1, p2):
    new_p = gr.Point(p1.x - p2.x, p1.y-p2.y)
    return new_p
t=0
f=0
tx = 0.1
n=0
def angle(t): return 20 * math.sin(9.81**0.5 * t + math.pi)
while True:
    cls()
    if n == 0:
        if t < 0.08:
            t += 0.01*tx
        else: n = 1
    if n == 1:
        if t > 0.025:
            t-=0.01*tx
        else: n = 0
    f = angle(t)
    print(coords.x-l*math.sin(f),coords.y-l*math.cos(f),t,n)
    ccl = gr.Circle(gr.Point(coords.x-l*math.sin(f),coords.y-l*math.cos(f)), 10)
    ccl.setFill('red')
    ccl.draw(window)
    gr.time.sleep(0.05)
