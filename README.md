# Todo

### Welcome to Todo-cli
**A simple command line based TODO application to manage your tasks.**

*If you are a terminal-oriented developer you will love it!*
### Features

- Quickly add task. 
- Searches date in task description and schedule task automatically.
- Create project and add related tasks together and later easily add them to today list to finish it.
- Delete and Update project and task description easily.
- Create labels for tasks
- Get list of overdue, today and upcoming tasks
- Two theme available 
- Sync tasks with firebase realtime database (setup required).
- Mail your tasks to someone.
- Print tasks in pdf format.

### Platforms
- Linux (any distribution)
- Mac OS X
- Windows (extra setup may be required)
### Setup

Make sure you have **`python`** and **`git`** installed in your system then,
Run following commands on your terminal.
```
$ git clone https://github.com/sumit-kushwah/todo.git
$ cd todo
$ pip3 install -r requirements.txt
$ python3 createalias.py
add below line to your shell configuration file (i.e .zshrc or .bashrc).
alias todo='/Users/sumitkushwah/Desktop/CWP/todo/todo'
```
After successfully creating alias you will be able to use this application.
You can try **`list`** command like this-
```
$ todo list
No task found.
```
If you have any issue while setting up please let me know [here](https://github.com/sumit-kushwah/todo/issues/new).

### Available commands

These are following available commands with their description.

| Command  | Description                            | 
|:-------  |:-------------------------------------- |
|    add   |Add one or more tasks                   |
|   list   |List out tasks                          |
|   find   |Find tasks by text or #label            |
|   update |Update tasks description or project name|
|   delete |Delete tasks or project                 |
|   sync   |Sync tasks with firebase                |
|   mail   |Share your tasks list using mail        |
|   print  |Print tasks as pdf file                 |

### How to use commands!

**1. To see available commands**
```
$ todo --help
```
**2. To see arguments within command**
```
$ todo <command> --help
```
**3. To use `sync` and `mail` command, change [config.py](https://github.com/sumit-kushwah/todo/blob/master/config.py)**

First create a project in firebase (see ) and then create realtime database ([see tutorial](https://firebase.google.com/docs/database)),
Set these three variables as following.

config.py
```python
# firebase settings
firebaseSDKFile = "<folder-path>/firebase.json"
databaseUrl = "https://todo-xyz.firebaseio.com/"

# mail settings
mailusername = "<your_gmail_username>"
```
In this project to send mail we are using [yagmail module](https://pypi.org/project/yagmail/) which requires keyring setup which is very easy to setup.

To set keyring for yagmail run this python script:

```python
import yagmail
yagmail.register('gmailusername', 'gmailpassword')
```

**4. To use `print` command**

You need to install `wkhtmltopdf`
#### Install

MacOS: `brew install Caskroom/cask/wkhtmltopdf`

Debian/Ubuntu: `apt-get install wkhtmltopdf`

Windows: `choco install wkhtmltopdf`


### Contributing change

If you found any issue or want to see a new feature please admit it by creating an new issue or by sending a pull request.


Happy todoing! :smiley: 
