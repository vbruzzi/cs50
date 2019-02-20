import re
from flask import Flask, abort, redirect, render_template, request, url_for

from helpers import add_csv, read_csv, delete_line
from werkzeug.exceptions import default_exceptions, HTTPException

app = Flask(__name__)

app.config["TEMPLATES_AUTO_RELOAD"] = True

@app.route("/")
def index():
    return render_template("form.html")
    
@app.route("/add", methods=["POST"])
def add():
    task = request.form.get("todo")
    due = request.form.get("date")
    if not request.form.get("todo") and not request.form.get("date"):
        abort(400, "Missing the task or the date")
    print(due)
    urgent = request.form.get("urgent")
    if not request.form.get("todo"):
        abort(400, "missing task")
    
    add_csv(task, due, urgent)
    
    return redirect(url_for('sheet'))
    
    
@app.route("/sheet", methods=["GET"])
def sheet():
    return render_template("sheet.html", tasks=read_csv())

@app.route("/delete", methods=["POST"])
def delete():
    taskId = request.args.get("taskId")
    delete_line(taskId)
    return redirect(url_for('sheet'))


#ERROR HANDLING
@app.errorhandler(HTTPException)
def errorhandler(error):
    return render_template("error.html", error=error), error.code