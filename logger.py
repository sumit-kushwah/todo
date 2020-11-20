def NoTasklogger(self, tasks, message, messageColor=bcolors.WARNING):
        if (len(tasks.keys()) == 0):
            print(messageColor + message + bcolors.ENDC)
            return True
        else:
            return False
    
def simpleLogger(self, message, messageColor=None):
    print(messageColor + message + bcolors.ENDC)