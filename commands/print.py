import pydf
from utils import htmlgenerator
from commands import listit

def print(args):
    data = listit.getTasksAndTitle(args)
    htmltext = htmlgenerator.generate(data["tasks"], data["title"])
    pdf = pydf.generate_pdf(htmltext)
    filename = args.filename or "~/Downloads/todos.pdf"
    with open(filename, 'wb') as f:
        f.write(pdf)
    f.close()
