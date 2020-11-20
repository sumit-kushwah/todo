import json
import datetime
from tasksutils import *
from config import *

class TasksGetter:
    def __init__(self, project=None):
        self.project = project
        with open(dbfilepath, 'r') as f:
            self.tasks = dictToTaskObjects(dict(json.load(f)))
            f.close()
        
        if project is not None:
            self.tasks = self.getProjectTasks()

    def getTodayTasks(self):
        todayTasks = []
        for task in self.tasks:
            if task.isTodayTask():
                todayTasks.append(task)
        return todaytasks

    def getProjectTasks(self):
        projectTasks = []
        for task in self.tasks:
            if task.projectMatched(self.project):
                projectTasks.append(task)
        return projectTasks

    def getTasks(self):
        return self.tasks
    
    def getTasksBySearch(self, searchtext):
        foundTasks = []
        for task in self.tasks:
            if task.searchTextFound(searchtext):
                foundTasks.append(task)
        return foundTasks
    
    def getTasksByLabel(self, label):
        tasks = []
        for task in self.tasks:
            if label in task.labels:
                tasks.append(task)
        return tasks
    
    def getDueTasks(self):
        dueTasks = []
        for task in self.tasks:
            if task.isDueTask():
                dueTasks.append(task)
        return dueTasks
    
    def getUpcomingTasks(self):
        upcomingTasks = []
        for task in self.tasks:
            if task.isUpcomingTask():
                upcomingTasks.append(task)
        return upcomingTasks