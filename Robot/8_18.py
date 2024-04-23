from pyrob.api import *
from funcs.py import *

@task
def task_8_18():
    x=0
    while not wall_is_on_the_right():
        if wall_is_above():
            fill_cell()
            move_right()
        if not wall_is_above() and not wall_is_on_the_right():
            while not wall_is_above():
                move_up()
                if cell_is_filled():
                    x+=1
                fill_cell()
            while not wall_is_beneath():
                move_down()
            move_right()
    mov('ax',x)


if __name__ == '__main__':
    run_tasks()