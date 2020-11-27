from fm import get, save
from task import Task
from colors import *

def makeDescriptions(words):
    descriptions = []
    description = ''
    for word in words:
        if word == ',' and description != '':
            descriptions.append(description)
            description = ''
        description = description + word + ' '
    
    if description != '':
        descriptions.append(description)
    return descriptions


def tasks(words, project=None):
    tasks = get()
    descriptions = makeDescriptions(words)
    for description in descriptions:
        tasks.append(Task(description=description, project=project))
    save(tasks)
    print(bcolors.OKGREEN + str(len(descriptions)) + ' task added successfully!')