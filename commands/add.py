from utils import fm
from utils.colors import *
from task import Task

def tasks(descriptions, project=None):
    tasks = fm.get()
    for description in descriptions:
        tasks.append(Task(description=description, project=project))
    fm.save(tasks)
    print(bcolors.OKGREEN + str(len(descriptions)) + ' task added!')