from task import *

def dictToTaskObjects(tasksdict):
    tasks = []
    for taskdict in tasksdict.values():
        tasks.append(Task().fromdict(taskdict))
    return tasks

def taskObjectsToDict(tasks):
    for task in tasks:
        tasksdict[task.id] = task.getdict()
    return tasksdict