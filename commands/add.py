from utils import fm
from utils.colors import *
from task import Task

def projectPrompt(project):
    if project is None:
        return ''
    return " in " + bcolors.BOLD + bcolors.OKBLUE + project + bcolors.OKGREEN + " project."

def tasks(descriptions, project=None):
    tasks = fm.get()
    for description in descriptions:
        tasks.append(Task(description=description, project=project))
    fm.save(tasks)
    print(bcolors.OKGREEN + "Ok! " + str(len(descriptions)) + ' task added' + projectPrompt(project))