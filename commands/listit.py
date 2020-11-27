from fm import get, save
from utils import prompter
from colors import bcolors

tasks = get()

def today():
    todayTasks = []
    for task in tasks:
        if task.isToday():
            todayTasks.append(task)
    return todayTasks

def all():
    return tasks
    
def dues():
    dues = []
    for task in tasks:
        if task.isDue():
            dues.append(task)
    return dues

def upcoming():
    upcoming = []
    for task in tasks:
        if task.isUpcoming():
            upcoming.append(task)
    return upcoming

def filterByProject(tasks, project):
    if project is None:
        return tasks
    ptasks = []
    for task in tasks:
        if task.ofProject(project):
            ptasks.append(task)
    return ptasks

def projectTasks(project):
    ptasks = []
    for task in tasks:
        if task.ofProject(project):
            ptasks.append(task)
    return ptasks

def todayIds(tasks):
    ids = []
    for task in tasks:
        if task.isToday():
            ids.append(task.id)
    return ids

def delete(ids):
    for task in tasks:
        if task.id in ids:
            tasks.remove(task)
    save(tasks)

def toToday(ids):
    for task in tasks:
        if task.id in ids:
            task.scheduleToToday()
    save(tasks)

def list(args):
    title = "Today Tasks"
    defaultIds = []
    deleteMode = True
    tasks = today()
    if args.all:
        title = "All Tasks"
        tasks = all()
        defaultIds = todayIds(tasks)
        deleteMode = False
    if args.due:
        title = "Overdue Tasks"
        tasks = dues()
        deleteMode = False
    if args.upcoming:
        title = "Upcoming Tasks"
        tasks = upcoming()
        deleteMode = False
    if args.project:
        tasks = filterByProject(tasks, args.project)
        deleteMode = False

    ids = prompter.prompt(tasks, title, defaultIds, args.verbose, args.sort)
     
    if len(ids) == 0:
        return

    if deleteMode:
        delete(ids)
        prompter.completeMsg(len(ids))
    else:
        toToday(ids)
        prompter.scheduleMsg(len(ids))