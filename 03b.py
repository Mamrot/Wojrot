path = r"C:\Users\admin\Desktop\Wojrot\tekst.txt"

dictionary = {"i": "oraz",
           "oraz": "i",
           "nigdy": "prawie nigdy",
           "dlaczego": "czemu"}

tekst = []

with open(path, 'r') as f:
    for line in f:
        for word in line.split():
            try:
                tekst.append(dictionary[word])
            except(KeyError):
                tekst.append(word)

print(tekst)
input("Wciśnij dowolny klawisz by kontynuować")