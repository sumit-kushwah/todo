#!/usr/bin/env python3

import argparse
import sys
from manager import *
sys.path.insert(0, './utils')
from taskslister import *
from tasksmodifier import *
from projecthandler import *

parser = argparse.ArgumentParser(prog="todo", description='A smart command line todo application.')
group = parser.add_mutually_exclusive_group()
group.add_argument("-a", "--add", help="add task", nargs='+')
group.add_argument("-l", "--list", help="list tasks", action="store_true")
group.add_argument("-due", "--overdue", help="list  overdue tasks", action="store_true")
group.add_argument("--deleteproject", help="delete a project")
group.add_argument("--projects", help="list projects", action="store_true")
group.add_argument("-u", "--upcoming", help="list upcoming tasks", action="store_true")
parser.add_argument("-p", "--project", help="specify project name")
args = parser.parse_args()

if (len(sys.argv) == 1):
    parser.print_help()
    sys.exit(1)

tl = TasksLister(args.project)
tm = TasksModifier()
ph = ProjectsHandler()

if args.add:
    tm.addTasks(args.add, args.project)
if args.list:
    tl.showTodayTasks()
if args.overdue:
    tl.showDueTasks()
if args.upcoming:
    tl.showUpcomingTasks()
if args.projects:
    ph.showProjects()
if args.deleteproject:
    ph.deleteProject(args.project)
