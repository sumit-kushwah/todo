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
        count = 0
        for task in self.tasks:
            if task.project == project:
                self.tasks.remove(task)
                count += 1
        self.saveTasks()
        print(bcolors.OKGREEN + str(count) + " tasks deleted." + bcolors.ENDC)
    
    def showProjects(self):
        projects = set(())
        for task in self.tasks:
            projects.add(task.project)
        print("projects\n" + bcolors.OKBLUE)
        for project in projects:
            print("* " + project , bcolors.OKGREEN)