from pyrob.api import *
from funcs.py import *

@task
def task_2_1():
    move_right(2)
    move_down()
    drawkrest()
    move_left()


if __name__ == '__main__':
    run_tasks()