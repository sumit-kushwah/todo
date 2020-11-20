import datetime
import uuid
import re
from taskutils import *

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
        self.project = dictobj["project"]
        self.id = dictobj["id"]
        self.date = dictobj["date"]
        self.labels = dictobj["labels"]
        self.description = dictobj["description"]
        return self

    def getdict(self):
        return vars(self)

    def isTodayTask(self):
        if self.date is None:
            return False
        taskdate = datetime.date(self.date.year, self.date.month, self.date.day)
        today = datetime.datetime.today()
        if (taskdate == today):
            return True
        else:
            return False
    
    def projectMatched(self, project):
        if self.project is None:
            return False
        if (self.project == project):
            return True
        return False

    def searchTextFound(self, text):
        if re.search(lower(text), lower(self.description)):
            return True
        
        return False
    
    def scheduleToToday(self):
        self.date = datetime.datetime.today()

    def isDueTask(self):
        if self.date < datetime.datetime.today():
            return True
        return False
    
    def isUpcomingTask(self):
        tomorrow = datetime.datetime.today() + datetime.timedelta(days = 1)
        if self.date >= tomorrow:
            return True
        return False
