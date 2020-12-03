import pdfkit
from utils import htmlgenerator
from commands import listit
from utils.colors import bcolors
from config import home

df = home + "/Downloads/" # downloading folder

def print(args):
    data = listit.getTasksAndTitle(args)
    htmltext = htmlgenerator.generate(data["tasks"], data["title"])
    # pdf = pydf.generate_pdf(htmltext)
    filename = df + (args.filename or "todos.pdf")
    try:
        pdfkit.from_string(htmltext, filename)
        print(bcolors.OKCYAN + "pdf generated check your download folder.")
    except:
        print(bcolors.FAIL + "Some error occurred while generating pdf.")
