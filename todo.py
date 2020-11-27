#!/usr/bin/env python3

from commands import listit, add, find
from parser import args, parser

# subcommand checking

def run(command, args):
    if command == 'add':
        add.tasks(args.descriptions, args.project)
    if command == 'list':
        listit.list(args)
    if command == 'find':
        find.find(args)


if args.command:
    command = args.command
    run(command, args)
else:
    parser.print_help()
