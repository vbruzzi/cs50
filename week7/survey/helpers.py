import csv
from datetime import datetime

#GLOBAL VARIABLE FOR THE CSV FILE
file = "survey.csv"

def add_csv(task, due, urgent):
    todo = [1, task, due, urgent]
    with open(file, 'r+', newline='') as csvFile:
        lines = csvFile.readlines()
        #CREATES AN ID IF THERE IS ALREADY A TASK
        if len(lines) != 0:    
            lastLine = lines[-1].split(",")
            todo[0] = int(lastLine[0]) + 1
        writer = csv.writer(csvFile)
        writer.writerow(todo)
    
    
def read_csv():
    todos = []
    noturgent = []
    with open(file, 'r') as csvFile:
        reader = csv.reader(csvFile, delimiter=',')
        # ADDS URGENT TASKS TO ONE LIST AND NON-URGENTO TO ANOTHER
        for row in reader:
            if row[3] == "on":
                todos.append(row)
            else:
                noturgent.append(row)
    #NOW ADDS THE NON-URGENTS TO THE MAIN LIST
    for task in noturgent:
        todos.append(task)    
    return todos
            

def delete_line(taskId):
    todos = read_csv()
    with open(file, 'w', newline='') as csvFile:
        writer = csv.writer(csvFile)
        for row in todos:
            if row[0] == taskId:
                continue
            writer.writerow(row)