print("""
*************************************

       SAYI TAHMIN OYUNU 

          HOSGELDINIZ

*************************************

""")
print("0 ile 100 arasinda bir sayi tuttum. Hadi tahmin edin!!!\n")
import random
x = random.randint(1, 100)
while True:
    y = int(input("Lutfen sayi giriniz: "))
    if x == y:
        print("Tahmininiz Dogru: ", y)
        continue
    elif x != y:
        if x > y:
            print("\nDaha BUYUK bir sayi giriniz!\n")
        else:
            print("\nDaha KUCUK bir sayi giriniz!\n")