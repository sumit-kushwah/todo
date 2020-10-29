import os
from colors import *

stream = os.popen("echo \{\} > ~/tasks.json")
stream = os.popen('touch temp.py')
stream = os.popen('cp todo.py temp.py')
stream = os.popen('chmod +x temp.py')
stream = os.popen('mv temp.py todo') # command as todo
cwd = os.getcwd()
print(bcolors.WARNING + f'alias todo=\'{cwd}/todo\'' + bcolors.ENDC)

# stream = os.popen('cd ..')



