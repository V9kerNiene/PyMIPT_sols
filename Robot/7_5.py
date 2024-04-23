from pyrob.api import *
from funcs.py import *

@task
def task_7_5():
    n = 0
    g = 0
    move_right()
    fill_cell()
    while not wall_is_on_the_right():
        move_right()
        if g == n:
            fill_cell()
            n += 1
            g=0
        else:
            g += 1


if __name__ == '__main__':
    run_tasks()