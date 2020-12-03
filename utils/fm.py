# task file manager

import json
from config import dbfilepath
from task import *

def dictToTaskObjects(tasksdict):
    tasks = []
    for taskdict in tasksdict.values():
        tasks.append(Task().fromdict(taskdict))
    return tasks

def taskObjectsToDict(tasks):
    tasksdict = {}
    for task in tasks:
        tasksdict[task.id] = task.getdict()
    return tasksdict

def get():
    with open(dbfilepath, 'r') as f:
        tasks = dictToTaskObjects(dict(json.load(f)))
    f.close()
    return tasks

def save(tasks):
    tasksdict = taskObjectsToDict(tasks)
    with open(dbfilepath, 'w') as f:
        json.dump(tasksdict, f)
    f.close()
