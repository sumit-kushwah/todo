import json
import datetime
from tasksutils import *
from config import *
from tasksdisplayer import *

class TasksLister:
    def __init__(self, project=None):
        self.project = project
        with open(dbfilepath, 'r') as f:
            self.tasks = dictToTaskObjects(dict(json.load(f)))
            f.close()
        
        title = (project or 'Today') + " tasks"

        self.td = TasksDisplayer(title, self.tasks, project)

    def showTodayTasks(self):
        todayTasks = []
        for task in self.tasks:
            if task.isTodayTask():
                todayTasks.append(task)
        self.td.tasks = todayTasks
        self.td.showTasksList()

    def showProjectTasks(self):
        projectTasks = []
        for task in self.tasks:
            if task.projectMatched(self.project):
                projectTasks.append(task)
        self.td.tasks = projectTasks
        self.td.showTasksList()

    def showAllTasks(self):
        self.td.showTasksList()
    
    def showTasksBySearch(self, searchtext):
        foundTasks = []
        for task in self.tasks:
            if task.searchTextFound(searchtext):
                foundTasks.append(task)
        self.td.tasks = foundTasks
        self.td.showTasksList()
    
    def showTasksByLabel(self, label):
        tasks = []
        for task in self.tasks:
            if label in task.labels:
                tasks.append(task)
        self.td.tasks = tasks
        self.td.showTasksList()
    
    def showDueTasks(self):
        dueTasks = []
        for task in self.tasks:
            if task.isDueTask():
                dueTasks.append(task)
        self.td.tasks = dueTasks
        self.td.showTasksList()
    
    def showUpcomingTasks(self):
        upcomingTasks = []
        for task in self.tasks:
            if task.isUpcomingTask():
                upcomingTasks.append(task)
        self.td.tasks = upcomingTasks
        self.td.showTasksList()