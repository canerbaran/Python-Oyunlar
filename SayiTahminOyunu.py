print(
"""
---------------------------
     SAYI TAHMIN OYUNU

      by Caner Baran
---------------------------
""")
import sys
from random import randint
a = randint(1, 9)
b = randint(0, 9)
c = randint(0, 9)
d = randint(0, 9)
while not (a!=b and b!=c and c!=a and a!=d and b!=d and c!=d):
    a = randint(1, 9)
    b = randint(0, 9)
    c = randint(0, 9)
    d = randint(0, 9)
liste = [a,b,c,d]
y = [str(i) for i in liste]
print("_ _ _ _\n")
dongu = 0
while True:
    x = str(input("\nSayi Giriniz: "))
    dogru = [i for i, j in zip(x, y) if i == j]
    yanlis = list(set(x) & set(y))
    if len(dogru) == 4 :
        print("TEBRIKLER TAHMININIZ DOGRU!!!")
        break
    elif len(yanlis) == 0:
        print("\nSifir")
    elif dogru != None:
        print("\n{}|  +{}  -{}".format(x, len(dogru), len(yanlis) - len(dogru)))
    else:
        print("{} - ".format(len(yanlis)))
    dongu += 1
    print("Tahmin Sayisi: {}".format(dongu))
