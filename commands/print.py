import pdfkit
from utils import htmlgenerator
from commands import listit

def print(args):
    data = listit.getTasksAndTitle(args)
    htmltext = htmlgenerator.generate(data["tasks"], data["title"])
    # pdf = pydf.generate_pdf(htmltext)
    filename = ("Users/sumitkushwah/Downloads" + args.filename) or "/Users/sumitkushwah/Downloads/todos.pdf"
    try:
        pdfkit.from_string(htmltext, filename)
    except:
        print("Some failure occurred while generating pdf.")
