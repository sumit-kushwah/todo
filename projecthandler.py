from config import *
from tasksutils import *
import json

class ProjectsHandler:
    def __init__(self):
        with open(dbfilepath, 'r') as f:
            self.tasks = dictToTaskObjects(dict(json.load(f)))
            f.close()

    def saveTasks(self):
        tasksdict = taskObjectsToDict(self.tasks)
        with open(dbfilepath, 'w') as f:
            json.dump(tasksdict, f)
        f.close()

    def deleteProject(self, project):
        for task in self.tasks:
            if task.project == project:
                self.tasks.remove(task)
        self.saveTasks()
    
    def getProjects(self):
        projects = set(())
        for task in self.tasks:
            projects.add(task.project)
        return list(projects)