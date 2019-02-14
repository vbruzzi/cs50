import csv

def add_csv(task, due, urgent):
    todo = [task, due, urgent]

    with open('todo.csv', 'a') as csvFile:
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
            