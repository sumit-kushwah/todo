import yagmail
from commands import listit
from config import mailusername
from utils import htmlgenerator

yag = yagmail.SMTP(mailusername)

def send(args):
    data = listit.getTasksAndTitle(args)
    htmltext = htmlgenerator.generate(data["tasks"], data["subject"])
    yag.send(args.tos, data["subject"], htmltext)
