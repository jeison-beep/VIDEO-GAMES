from random import randint
import os
def dices():
    d1 = randint (1,6)
    d2 = randint (1,6)
    return d1,d2


os.system('clear')
d=dices()

print ("dice 1:" ,d[0])
print (f"dice 1: {d[1]}")

if d[0] ==d [1]:
    print ("You Win")
else:
    print ("you lose")