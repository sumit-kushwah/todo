from fm import get, save

tasks = get()

def deleteTask(id):
    for task in tasks:
        if task.id == id:
            tasks.remove(task)
            save(tasks)
            print(f"Task with id {id} deleted!")
            return
    print("No task found with this task-id")

def deleteProject(project):
    count = 0
    for task in tasks:
        if task.project == project:
            tasks.remove(task)
            count += 1
    saveTasks(tasks)
    if count == 0:
        print("No project found with project name.")
        return
    print(str(count) + " tasks deleted.")

    
def delete(args):
    if args.project:
        deleteProject(args.project)
    if args.taskid:
        deleteTask(args.taskid)