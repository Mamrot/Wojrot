import os
def policzPliki(path):

    for i in os.listdir(path):
        if os.path.isdir(path + r'\\' + i):
            policzPliki(path + r'\\' + i)

        else:
            print(i)

policzPliki(r'C:\Xilinx\Vivado\2019.1\tps\win64\git-2.16.2')
input("Wciśnij dowolny klawisz by kontynuować")
