import argparse

parser = argparse.ArgumentParser(prog="todo", description='A simple command line todo application.')
subparsers = parser.add_subparsers(title="Commands", description='Available Commands', help='commands', dest="command")

"""
    **commands**
    command   description                   default flags

    add       add one or more tasks         none    --project(-p)
    list      list tasks                    none    --all, --due, --upcoming --sortby [ask question]  --verbose (show project name, taskid) --project
    find      find tasks by text, label     none    none
    update    update task or project        none    --project, --taskid (if project is specified then project name updated) both must be mutually exclusive
    delete    delete task or project        none    --project, --taskid (if project is specified then project name deleted)
    sync      sync tasks to firebase        none    none
    mail      mail tasks                    none    none
    print     print tasks in pdf format     none    none
    reset     reset the application         none    none

"""

# parser for add command

parser_add = subparsers.add_parser('add', help="add one or more tasks")
parser_add.add_argument('descriptions', nargs='+', help='task descriptions')
parser_add.add_argument('-p', '--project', help='project name')

# parser for list command

parser_list = subparsers.add_parser('list', help='list out tasks')
listgroup = parser_list.add_mutually_exclusive_group()
listgroup.add_argument('-a', '--all', action='store_true', help='list out all tasks')
listgroup.add_argument('-d', '--due', action='store_true', help='list out overdue tasks')
listgroup.add_argument('-u', '--upcoming', action='store_true', help='list out upcoming tasks')
parser_list.add_argument('-p', '--project', help='project name')
parser_list.add_argument('--sort', action='store_true', help='sort tasks by name, date etc.')
parser_list.add_argument('--verbose', '-v', action='count', help='verbosity label', default=0)

# parser for find command

parser_find = subparsers.add_parser('find', help="find tasks by text or #label")
parser_find.add_argument('text', help="text or #label")
parser_find.add_argument('--sort', action='store_true', help='sort tasks by name, date etc.')
parser_find.add_argument('--verbose', '-v', action='count', help='verbosity label', default=0)

# parser for update command

parser_update = subparsers.add_parser('update', help='update tasks description or project name')
updategroup = parser_update.add_mutually_exclusive_group()
updategroup.add_argument('-id', '--taskid', help='id of task')
updategroup.add_argument('-p', '--project', help='project name')

# parser for delete command

parser_delete = subparsers.add_parser('delete', help='delete tasks or project')
deletegroup = parser_delete.add_mutually_exclusive_group()
deletegroup.add_argument('-id', '--taskid', help='id for task')
deletegroup.add_argument('-p', '--project', help='project name')

# parser for sync command

parser_sync = subparsers.add_parser('sync', help='Sync tasks with firebase')
syncgroup = parser_sync.add_mutually_exclusive_group()
syncgroup.add_argument('--pull', help='get tasks from firebase', action='store_true')
syncgroup.add_argument('--push', help='save tasks to firebase', action='store_true')

# parser for mail command

parser_mail = subparsers.add_parser('mail', help='Mail tasks')
parser_mail.add_argument('tos', help='receiver gmail ids', nargs="+")
mailgroup = parser_mail.add_mutually_exclusive_group()
mailgroup.add_argument('-a', '--all', action='store_true', help='list out all tasks')
mailgroup.add_argument('-d', '--due', action='store_true', help='list out overdue tasks')
mailgroup.add_argument('-u', '--upcoming', action='store_true', help='list out upcoming tasks')
parser_mail.add_argument('-p', '--project', help='project name')
parser_mail.add_argument('--subject', help='Subject of mail message')


# parser for print command

parser_print = subparsers.add_parser('print', help='Print tasks')
parser_print.add_argument('-f', '--filename', help='File name')

# parsing the arguments

args = parser.parse_args()