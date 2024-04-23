from pyrob.api import *
from funcs.py import *

@task
def task_2_2():
    move_right()
    move_down()
    for _ in range(4):
        drawkrest()
        move_right(4)
    drawkrest()
    move_left()


if __name__ == '__main__':
    run_tasks()