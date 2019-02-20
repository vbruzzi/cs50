import csv
from datetime import datetime

def add_csv(task, due, urgent):
    ## TODO --- ADD ID GENERATION
    todo = [1, task, due, urgent]
    with open('todo.csv', 'a', newline='') as csvFile:
        writer = csv.writer(csvFile)
        writer.writerow(todo)
    
    csvFile.close()
    
    
def read_csv():
    todos = []
    with open('todo.csv', 'r') as csvFile:
        reader = csv.reader(csvFile, delimiter=',')
        for row in reader:
            todos.append(row)
            
    return todos
            

def delete_line(taskId):
    todos = read_csv()
    with open('todo.csv', 'w', newline='') as csvFile:
        writer = csv.writer(csvFile)
        for row in todos:
            if row[0] == taskId:
                continue
            writer.writerow(row)

def sort_csv():
    print("YUH")
    with open('todo.csv', 'a', newline='') as csvFile:
        reader = csv.reader(csvFile, delimiter=',')
        sortedData = reader(reader, key=operator.itemgetter(0),reverse=False)
        print(sortedData)