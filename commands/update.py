from utils import fm
import inquirer

tasks = fm.get()

def textAsk(title, message):
    questions = [ inquirer.Text(title, message) ]
    answer = inquirer.prompt(questions)
    return answer[title]

def updateTask(id, description):
    for task in tasks:
        if task.id == id:
            task.updateDescription(description)
            fm.save(tasks)
            return
    print("No task found with this task-id")

def udpateProject(oldname, newname):
    count = 0
    for task in tasks:
        if task.project == oldname:
            count = count + 1
            task.updateProject(newname)
    if count > 0:
        fm.save(tasks)
        print("Project name updated")
    else:
        print(f"No project found with {oldname} name")

    
def update(args):
    if args.project:
        newname = textAsk("newname", "Enter new project name")
        updateProject(args.project, newname)
    if args.taskid:
        description = textAsk("desc", "Enter new task description")
        updateTask(args.taskid, description)