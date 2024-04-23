from pyrob.api import *
from funcs.py import *

@task
def task_9_3():
    n = -1
    while not wall_is_on_the_right():
        n+=1
        move_right()
    move_left(n)
    drawtr(n,0)
    move_right(n)
    move_down(n)
    drawtr(n,1)
    move_down()
    move_left(n)
    drawtr(n,2)
    move_left()
    move_up(n)
    drawtr(n,3)
    move_down(n)


if __name__ == '__main__':
    run_tasks()