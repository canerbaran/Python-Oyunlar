print("""
*************************************

    Multiplication Game

        Welcome

*************************************

""")
import random

while True:
    x = random.randint(1, 9)
    y = random.randint(1, 9)
    print("{} x {}\n".format(x, y))
    z = int(input("Please type the answer : "))
    while True:
        if z == x*y:
            print("Your Answer is True :) \n")
            continue
        else:
            False
            print("Try Again!!!")
