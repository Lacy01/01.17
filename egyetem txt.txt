import hiresek_alap

egyetemek=[]
for _ in range (3):
    egyetemnév=input("Add meg egy egyetem nevét! ")
    város=input("Add meg a az egyetem városát! ")
    orszag=input("Add mega nemzetiségét(a/n)! ")
    egyetem=hiresek.alap.HíresEgyetem(egyetemnév,város)
    egyetemek.append(egyetem)
for egyetemek in egyetem:
    print(f'{Egyetem.elotag()}. {Egyetem.egyetemnév}, egy híres {Egyetem.város}-i egyetem')