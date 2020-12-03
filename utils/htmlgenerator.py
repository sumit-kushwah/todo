def generate(tasks, title):
    html = f"<h2>{title}</h2>"
    html += "<ul>"
    for task in tasks:
        html += f"<li style=\"font-size: 20px;\">  {task.description} </li>"
    html += "</ul>"
    return html
