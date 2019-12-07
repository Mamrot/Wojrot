import json
file = open("json_wojrot.json","r")
file_content = file.read()
json_content = json.loads(file_content)
json_content["Dzisiaj"] = "Sroda"
str_content = json.JSONEncoder().encode(file_content)
print(str_content)

def read_tasks(file):
    with open(file) as fd:
        return json.loads(fd.read())

def write_tasks(file,tasks):
    with open(file,'w') as fd:
        fd.write(json.dumps(tasks))

def show_tasks(file):
    tasks = read_tasks(file)
    print('\n\n{:^50}'.format('TASKS'))
    print('-' * 50)
    for index,task in enumerate(tasks):
        print('{0} | {1:<33} | {2}'.format(index,task['task'],task['deadline']))

def add_task(task,deadline,file):
    tasks = read_tasks(file)
    tasks.append({'task':task,'deadline':deadline})
    write_tasks(file,tasks)
    return 0

wzrost = input("Podaj wzrost: ")
waga = input("Podaj wage: ")
wiek = input("Podaj wiek: ")
file = open("json_wojrot.json","w")

n = str(input("Wybierz działanie(+ dodaj/p pokaz): "))

if n == 'p':
    show_tasks(file)
elif n == '+':
    add_task(task,deadline,file)