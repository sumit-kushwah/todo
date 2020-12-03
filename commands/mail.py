import yagmail
from commands import listit
from config import mailusername
from utils import htmlgenerator
from utils.colors import *

yag = yagmail.SMTP(mailusername)

def send(args):
    data = listit.getTasksAndTitle(args)
    htmltext = htmlgenerator.generate(data["tasks"], data["title"])
    try:
        yag.send(args.tos, data["subject"], htmltext)
        print(bcolors.OKBLUE + "mail sent successfully!!")
    except:
        print(bcolors.FAIL + "Some error occurred while sending mail.")