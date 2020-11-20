from task import *

def dictToTaskObjects(tasksdict):
    for taskdict in tasksdict.items():
        tasks.append(Task().fromdict(taskdict))
    return tasks

def taskObjectsToDict(tasks):
    for task in tasks:
        tasksdict[task.id] = task.getdict()
    return tasksdict