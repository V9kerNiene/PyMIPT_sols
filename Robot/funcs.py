from pyrob.api import *
def drawkrest():
    fill_cell()
    move_down()
    fill_cell()
    move_down()
    fill_cell()
    move_left()
    move_up()
    fill_cell()
    move_right(2)
    fill_cell()
    move_up()
    move_left()
def drawline():
    drawkrest()
    for _ in range(9):
        move_right(4)
        drawkrest()
def drawtr(n=3,orientation=0):
    n1=n
    if orientation == 0:
        for _ in range(int(n/2+0.5)):
            if n >1:
                for __ in range(n-1):
                    fill_cell()
                    move_right()
                    fill_cell()
                move_left(n-1)
                move_down()
                move_right()
            else:
                fill_cell()
                move_up()
                move_left()
            n-=2
        if n1 > 3:
            move_up(int(n1/2+0.5)-2)
            move_left(int(n1/2+0.5)-2)
    elif orientation==2:
        for _ in range(int(n/2+0.5)):
            if n >1:
                for __ in range(n-1):
                    fill_cell()
                    move_right()
                    fill_cell()
                move_left(n-1)
                move_up()
                move_right()
            else:
                fill_cell()
                move_down()
                move_left()
            n-=2
        if n1 > 3:
            move_down(int(n1 / 2 + 0.5) - 2)
            move_left(int(n1 / 2 + 0.5) - 2)
    elif orientation==1:
        for _ in range(int(n/2+0.5)):
            if n >1:
                for __ in range(n-1):
                    fill_cell()
                    move_up()
                    fill_cell()
                move_down(n-1)
                move_left()
                move_up()
            else:
                fill_cell()
                move_right()
                move_down()
            n-=2
        if n1 > 3:
            move_down(int(n1 / 2 + 0.5) - 2)
            move_right(int(n1 / 2 + 0.5) - 2)
    elif orientation==3:
        for _ in range(int(n/2+0.5)):
            if n >1:
                for __ in range(n-1):
                    fill_cell()
                    move_down()
                    fill_cell()
                move_up(n-1)
                move_right()
                move_down()
            else:
                fill_cell()
                move_left()
                move_up()
            n-=2
        if n1 > 3:
            move_left(int(n1 / 2 + 0.5) - 2)
            move_up(int(n1 / 2 + 0.5) - 2)