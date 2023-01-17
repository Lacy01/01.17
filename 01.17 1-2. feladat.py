def isko(pont):
    if pont<1000:
        return True
    else:
        return False

nev=input("Add meg az iskola nevét! ")
pont=int(input("Add meg a pontszámát! "))
if True:
    print(f'{nev} egy kis létszámú iskola.')
else:
    print(f'{nev} egy nagy létszámú iskola.')



isk1=int(input("Adj meg az egyik iskolai számot! "))
isk2=int(input("Adjon meg egy másik iskolai számot! "))
if isk1<isk2:
    print("A látszám érték a másik iskolában több.")
elif isk1>isk2:
    print("A létszám az egyik iskolában több.")
else: 
    print("A két létszám egyenlő")



