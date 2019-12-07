import os

source = os.listdir(r'C:\Xilinx\Vivado\2019.1\tps\win64\git-2.16.2\dev')
count=0
for plik in source:
    count +=1
print("ilosc plikow:", count)

input("Wciśnij dowolny klawisz by kontynuować")



