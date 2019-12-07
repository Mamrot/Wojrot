import os

path = r"C:\Users\admin\Desktop\Wojrot"

source = os.listdir(path)

for i in source:
    os.rename(path + '\\' + i, path +'\\' + i[:-3] + 'png')

input("Wciśnij dowolny klawisz by kontynuować")