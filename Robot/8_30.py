from pyrob.api import *
from funcs.py import *

@task
def task_8_30():
    h=0
    while h!=1:
        while wall_is_beneath():
            n=0
            n1=0
            while not wall_is_on_the_left():
                move_left()
                if not wall_is_beneath():
                    n=1
                    break
            if n == 1:
                break
            while not wall_is_on_the_right():
                move_right()
                if not wall_is_beneath():
                    n1=1
                    break
            if n1 == 1:
                break
            if n1 == 0 and n == 0:
                h = 1
                break
        while not wall_is_beneath():
            move_down()
    while not wall_is_on_the_left():
        move_left()


if __name__ == '__main__':
    run_tasks()