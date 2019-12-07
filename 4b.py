import random

def fillTab(number,fromNumber,toNumber):
    table=[]
    while number>0:
        table.append(random.randint(fromNumber,toNumber))
        number -=1
    return table

def bubbleSort(tab):
    for i in range(len(tab)):
        j=len(tab)-1
        while j>i:
            if tab[j]<tab[j-1]:
                x=tab[j]
                tab[j]=tab[j-1]
                tab[j-1]=x
            j-=1
    return tab

tab=fillTab(10,1,100)
print("przed: \t"+str(tab))

newTab=bubbleSort(tab)
print("po: \t"+str(tab))



