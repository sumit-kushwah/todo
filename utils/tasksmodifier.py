import json
import datetime
from task import *
from tasksutils import *
from config import *

class TasksModifier:
    def __init__(self):
        with open(dbfilepath, 'r') as f:
            self.tasks = dictToTaskObjects(dict(json.load(f)))
            f.close()

    def saveTasks(self):
        tasksdict = taskObjectsToDict(self.tasks)
        with open(dbfilepath, 'w') as f:
            json.dump(tasksdict, f)
        f.close()
    
    def addTasks(self, descriptions, project):
        for description in descriptions:
            self.tasks.append(Task(description=description, project=project))
        self.saveTasks()
        print(bcolors.OKGREEN, str(len(descriptions) + ' tasks added successfully!'))
    
    def deleteTasks(self, tasksids):
        for task in self.tasks:
            if task.id in tasksids:
                self.tasks.remove(task)
        self.saveTasks()
    
    def scheduleTasksToToday(self, tasksids):
        for task in self.tasks:
            if task.id in tasksids:
                task.scheduleToToday()
        self.saveTasks()
