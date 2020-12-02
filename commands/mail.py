import yagmail
from commands import listit
from config import mailusername

yag = yagmail.SMTP(mailusername)

def htmlText(tasks, title):
    html = f"<h2>{title}</h2>"
    html += "<ul>"
    for task in tasks:
        html += f"<li style=\"font-size: 20px;\">  {task.description} </li>"
    html += "</ul>"
    return html


def send(args):
    data = listit.getmaillist(args)
    htmltext = htmlText(data["tasks"], data["subject"])
    yag.send(args.tos, data["subject"], htmltext)
