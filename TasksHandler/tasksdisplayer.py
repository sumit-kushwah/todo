import inquirer
from config import theme
from tasksmodifier import *

class TasksDisplayer:
    def __init__(self, title=None, tasks=None, project=None):
        self.title = title
        self.tasks = tasks
        self.project = project
    
    def showTasksList(self):
        choices = []
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
        else:
            modifier.scheduleTasksToToday(ids)