import json
import firebase_admin
from firebase_admin import db
import config
from task import Task
from utils import fm

dbfile = config.dbfilepath

cred = firebase_admin.credentials.Certificate(config.firebaseSDKFile)
firebase_admin.initialize_app(cred, {
    'databaseURL': config.databaseUrl
})

ref = db.reference('/')

def push():
    with open(dbfile, 'r') as f:
        tasksdict = dict(json.load(f))
    f.close()
    ref.set(tasksdict)

def pull():
    tasksdict = ref.get()
    tasks = []
    for id in tasksdict:
        tasks.append(Task().fromdict(tasksdict[id]))
    fm.save(tasks)

def sync(args):    
    if args.push:
        push()
        return
    if args.pull:
        pull()
        return
    print("Please specify atleast one option.")
        
