import datetime
import uuid
import re
from taskhelper import *

class Task:
    def __init__(self,
                 description=None,
                 project=None):
        if description is None:
            return
        self.project = project
        self.id = str(uuid.uuid4())
        self.date = dateFromText(description, project is not None)
        self.labels = labelsFromText(description)
        self.description = remExtras(description, self.labels)

    def fromdict(self, dictobj):
        self.id = dictobj["id"]
        self.description = dictobj["description"]
        try:
            self.project = dictobj["project"]
        except:
            self.project = None
        try:
            self.labels = dictobj["labels"]
        except:
            self.labels = []
        self.date = None
        try:
            self.date = datetime.datetime.fromisoformat(dictobj["date"])
        except:
            self.date = None
        return self

    def getdict(self):
        result =  vars(self)
        if result["date"]:
            result["date"] = str(result["date"])
        return result

    def isToday(self):
        if self.date is None:
            return False
        taskdate = self.date
        today = datetime.datetime.today()
        if (taskdate.year == today.year and
            taskdate.month == today.month and
            taskdate.day == today.day):
            return True
        else:
            return False
    
    def ofProject(self, project):
        if self.project is None:
            return False
        if (self.project == project):
            return True
        return False

    def isTextFound(self, text):
        if re.search(text.lower(), self.description.lower()):
            return True
        
        return False
    
    def scheduleToToday(self):
        self.date = datetime.datetime.today()

    def isDue(self):
        if self.date < datetime.datetime.today():
            return True
        return False
    
    def isUpcoming(self):
        tomorrow = datetime.datetime.today() + datetime.timedelta(days = 1)
        if self.date >= tomorrow:
            return True
        return False

    def updateDescription(self, newDescription):
        if newDescription == '':
            print("New description should not be empty")
            return
        self.description = newDescription
        print(f"Task with id {self.id} updated successfully!")
    
    def updateProject(self, newProject):
        if newProject == '':
            print("New project name should not be empty")
            return
        self.project = newProject