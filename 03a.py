path = r"C:\Users\admin\Desktop\Wojrot\tekst.txt"

#print(path)

tekst = []

with open(path, 'r') as f:
    for line in f:
        for word in line.split():
            if word != 'oraz' and word != 'i' and word !='prawie' and word !='nigdy' and word !='czemu' :
                tekst.append(word)

print(tekst)
input("Wciśnij dowolny klawisz by kontynuować")