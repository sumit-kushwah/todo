#!/usr/bin/env python3

import argparse
import sys
from manager import *

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

manager = Manager()

if args.add:
    manager.addTasks(args.add, args.project)
if args.list:
    manager.listTasks(args.project)
if args.overdue:
    manager.listDueTasks(args.project)
if args.upcoming:
    manager.listUpcomingTasks(args.project)
if args.projects:
    manager.listProjects()
if args.deleteproject:
    manager.deleteProject(args.project)
