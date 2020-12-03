import inquirer
from config import theme
from utils import colors

def scheduleMsg(length):
    if length == 0:
        return 
    print(bcolors.OKGREEN + str(length) + " task scheduled to today." + bcolors.ENDC)

def completeMsg(length):
    if length == 0:
        return
    print(bcolors.OKGREEN + str(length) + " task completed." + bcolors.ENDC)

def sortTasks(tasks):
    choices = ["name", "date"]
    questions = [
        inquirer.List('option',
            message='Select one sorting method',
            choices=choices)
    ]

    option = inquirer.prompt(questions, theme=theme)

    if option == "name":
        tasks.sort(key=description)
    if option == "date":
        tasks.sort(key=date)
    
    return tasks
 
def choicesMaker(tasks, vlabel=0):
    choices = []
    if vlabel == 0:
        for task in tasks:
            choices.append((task.description, task.id))
    if vlabel == 1:
        for task in tasks:
            choices.append((task.description + (task.project or ''), task.id))
    if vlabel >= 2:
        for task in tasks:
            choices.append((task.description + (task.project or '') + " " + task.id, task.id))
    return choices

def prompt(tasks, title=None, default=[], vlabel=0, sort=False):
    if len(tasks) == 0: 
        print(bcolors.WARNING + "No task found." + bcolors.ENDC)
        return []

    if sort:
        tasks = sortTasks(tasks)
        
    choices = choicesMaker(tasks, vlabel)

    if title is None:
        title = str(len(tasks)) + " tasks"

    questions = [
        inquirer.Checkbox('ids',
            message=title,
            choices=choices,
            default=default)
    ]

    ids = inquirer.prompt(questions, theme=theme)["ids"]
    return ids