import inquirer
from config import theme
from tasksmodifier import *
from logger import *
import bcolors

class TasksDisplayer:
    def __init__(self, title=None, tasks=None, project=None):
        self.title = title
        self.tasks = tasks
        self.project = project
    
    def showTasksList(self):
        choices = []
        if self.tasks is None or []: 
            print(bcolors.WARNING + "No task found." + bcolors.ENDC)
            return
        for task in self.tasks:
            choices.append(task.description, task.id)

        questions = [
            inquirer.Checkbox('taskids',
                message=title,
                choices=choices,
                default=default)
        ]

        ids = inquirer.prompt(questions, theme=theme)
        modifier = TasksModifier()
        if self.project is None:
            modifier.deleteTasks(ids)
            print(bcolors.OKGREEN + str(len(ids)) + " tasks deleted." + bcolors.ENDC)
        else:
            modifier.scheduleTasksToToday(ids)
            print(bcolors.OKGREEN + str(len(ids) + " tasks scheduled to today.") + bcolors.ENDC)
