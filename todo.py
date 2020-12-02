#!/usr/bin/env python3

from commands import listit, add, find, update, delete, sync
from parser import args, parser

# subcommand checking

def run(command, args):
    if command == 'add':
        add.tasks(args.descriptions, args.project)
    if command == 'list':
        listit.list(args)
    if command == 'find':
        find.find(args)
    if command == 'update':
        update.update(args)
    if command == 'delete':
        delete.delete(args)
    if command == 'sync':
        sync.sync(args)


if args.command:
    command = args.command
    run(command, args)
else:
    parser.print_help()
