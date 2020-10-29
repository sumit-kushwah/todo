import uuid
import json
import datetime
import inquirer
from colors import bcolors
from inquirer.themes import *

class Manager:
    def __init__(self):
        with open('./tasks.json', 'r') as f:
            self.tasks = dict(json.load(f))
            f.close()

    def listTasks(self, project=None):
        tasks = {}
        if (project is None):
            for taskid in self.tasks:
                task = self.tasks[taskid]
                if task["date"]:
                    if self.isTodayTask(task):
                        tasks[taskid] = task
            if self.NoTasklogger(tasks, "No task due for today."): return
            completedTasks = self.showCheckBoxList(tasks, "Today Tasks")
            taskids = completedTasks["taskids"]
            self.deleteTasks(taskids)
            self.simpleLogger(str(len(taskids)) + " task completed.", bcolors.OKGREEN)

        else:
            for taskid in self.tasks:
                if self.tasks[taskid]["project"] == project:
                    tasks[taskid] = self.tasks[taskid]
            if self.NoTasklogger(tasks, "This project has no task."): return
            movedTasks = self.showCheckBoxList(tasks, project + " Tasks")
            self.moveToToday(movedTasks["taskids"])
        

    def addTask(self, description, project=None):
        taskid = str(uuid.uuid4())
        listname = ''
        if (project is None):
            date = str(datetime.datetime.utcnow())
            listname = 'today.'
        else:
            date = None
            listname = project + ' project.'
        task = {
            "id": taskid,
            "project": project,
            "description": description,
            "date": date
        }

        self.tasks[taskid] = task
        self.saveTasks()
        self.simpleLogger("1 task added to " + listname , bcolors.OKGREEN)

    def deleteTasks(self, taskids):
        for taskid in taskids:
            try:
                self.tasks.pop(taskid)
            except KeyError:
                continue
        self.saveTasks()

    def moveToToday(self, taskids):
        for taskid in taskids:
            try:
                self.tasks[taskid]["date"] = str(datetime.datetime.utcnow())
            except KeyError:
                continue
        self.saveTasks()
        self.simpleLogger(str(len(taskids)) + " tasks moved to today list.", bcolors.OKBLUE)

    def saveTasks(self):
        with open('./tasks.json', 'w') as f:
            json.dump(self.tasks, f)
        f.close()
    
    def isTodayTask(self, task):
        taskdate = datetime.datetime.fromisoformat(task["date"])
        today = datetime.datetime.now()
        if (today.year == taskdate.year and
            today.month == taskdate.month and
            today.day == taskdate.day):
            return True
        else:
            return False
    
    def showCheckBoxList(self, tasks, message="Tasks"):
        choices = []
        for taskid in tasks:
            choices.append((tasks[taskid]["description"], taskid))
        questions = [
            inquirer.Checkbox('taskids',
                message=message,
                choices=choices)
        ]

        answers = inquirer.prompt(questions, theme=GreenPassion())
        return answers

    def NoTasklogger(self, tasks, message, messageColor=bcolors.WARNING):
        if (len(tasks.keys()) == 0):
            print(messageColor + message + bcolors.ENDC)
            return True
        else:
            return False
    
    def simpleLogger(self, message, messageColor=None):
        print(messageColor + message + bcolors.ENDC)
    
    def deleteProject(self, project):
        taskids = []
        for taskid in self.tasks:
            if (self.tasks["taskid"]["project"] == project):
                taskids.append(taskid)
        self.deleteTasks(taskids)
        self.simpleLogger(len(taskids) + " tasks deleted.", bcolors.OKWARNING)
    
    def listProjects(self):
        projects = set(())
        for taskid in self.tasks:
            project = self.tasks[taskid]["project"]
            if (project):
                projects.add(project)
        self.simpleLogger(str(len(projects)) + " projects\n" , bcolors.OKBLUE)
        
        for project in projects:
            self.simpleLogger("* " + project , bcolors.OKGREEN)
        
