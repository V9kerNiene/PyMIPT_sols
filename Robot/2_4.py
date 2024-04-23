from pyrob.api import *
from funcs.py import *

@task
def task_2_4():
    move_right()
    for _ in range(4):
        drawline()
        move_down(4)
        move_left(36)
    drawline()
    move_left(36)
    move_left()


if __name__ == '__main__':
    run_tasks()