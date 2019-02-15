import re
from flask import Flask, abort, redirect, render_template, request, url_for

from helpers import add_csv, read_csv

app = Flask(__name__)

app.config["TEMPLATES_AUTO_RELOAD"] = True

@app.route("/")
def index():
    return render_template("index.html")
    
@app.route("/add", methods=["POST"])
def add():
    task = request.form.get("todo")
    due = request.form.get("date")
    urgent = request.form.get("urgent")
    if not request.form.get("todo"):
        abort(400, "missing task")
    
    add_csv(task, due, urgent)
    
    return redirect(url_for('list'))
    
    
@app.route("/list", methods=["GET"])
def list():
    return render_template("list.html", tasks=read_csv())
    
@app.route("/delete", methods=["POST"])
def delete():
    taskId = request.form(taskId)
    print(taskId)
    return redirect(url_for('list'))