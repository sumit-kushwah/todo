import yagmail
from commands import listit
from config import mailusername, mailpassword

yag = yagmail.SMTP(mailusername, mailpassword)
contents = [
    "This is the body, and here is just text http://somedomain/image.png",
    "You can find an audio file attached.", '/local/path/to/song.mp3'
]

def send(args):
    data = listit.getmaillist(args)
    yag.send(args.tos, data["subject"], contents)
