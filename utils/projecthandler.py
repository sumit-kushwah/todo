import json
from config import *
from updater import saveTasks

with open(dbfilepath, 'r') as f:
    tasks = dictToTaskObjects(dict(json.load(f)))
    f.close()

def deleteProject(project):
    count = 0
    for task in tasks:
        if task.project == project:
            tasks.remove(task)
            count += 1
    saveTasks(tasks)
    print(bcolors.OKGREEN + str(count) + " tasks deleted." + bcolors.ENDC)

def showProjects():
    projects = set(())
    for task in tasks:
        projects.add(task.project)
    print("projects\n" + bcolors.OKBLUE)
    for project in projects:
        print("* " + project , bcolors.OKGREEN)