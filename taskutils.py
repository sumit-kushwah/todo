from dateparser.search import search_dates
import re
import datetime

def dateFromText(text, isprojecttask):
    dates = search_dates(text)
    if isprojecttask:
        if dates is None:
            return None
    else:
        if dates is None:
            return datetime.datetime.now()
    return dates[0][1]

def labelsFromText(text):
    regex = "#(\w+)"
    matches = re.findall(regex, text)
    return matches

def priorityFromText(text):
    regex = "@([0-9]+)"
    matches = re.findall(regex, text)
    return matches

def remExtras(text, matches):
    text = text.replace('#', '')
    for match in matches:
        text = text.replace(match, '')
    return text