from pyrob.api import *
from funcs.py import *

@task
def task_7_6():
    n = 0
    while  n < 5:
        move_right()
        if cell_is_filled():
            n+=1


if __name__ == '__main__':
    run_tasks()