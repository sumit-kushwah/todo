from utils import fm
from utils.colors import *

tasks = fm.get()

def deleteTask(id):
    for task in tasks:
        if task.id == id:
            tasks.remove(task)
            fm.save(tasks)
            print("Ok! " + bcolors.WARNING + f"Task with id {id} deleted.")
            return
    print(bcolors.FAIL + "No task found with this taskid.")

def deleteProject(project):
    count = 0
    for task in tasks:
        if task.project == project:
            tasks.remove(task)
            count += 1
    fm.save(tasks)
    if count == 0:
        print(bcolors.FAIL + "No project found with project name.")
        return
    print("Ok! " + bcolors.WARNING + str(count) + " tasks deleted with this project.")

    
def delete(args):
    if args.project:
        deleteProject(args.project)
    if args.taskid:
        deleteTask(args.taskid)