import csv
from datetime import datetime
from operator import itemgetter

def add_csv(task, due, urgent):
    todo = [1, task, due, urgent]
    with open('todo.csv', 'r+', newline='') as csvFile:
        lines = csvFile.readlines()
        #CREATES AN ID IF THERE IS ALREADY A TASK
        if len(lines) != 0:    
            lastLine = lines[-1].split(",")
            todo[0] = int(lastLine[0]) + 1
        writer = csv.writer(csvFile)
        writer.writerow(todo)
    csvFile.close()
    
    
def read_csv():
    todos = []
    noturgent = []
    with open('todo.csv', 'r') as csvFile:
        reader = csv.reader(csvFile, delimiter=',')
        for row in reader:
            if row[3] == "on":
                todos.append(row)
            else:
                noturgent.append(row)

    for task in noturgent:
        todos.append(task)    
    return todos
            

def delete_line(taskId):
    todos = read_csv()
    with open('todo.csv', 'w', newline='') as csvFile:
        writer = csv.writer(csvFile)
        for row in todos:
            if row[0] == taskId:
                continue
            writer.writerow(row)