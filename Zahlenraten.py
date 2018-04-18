# zahlenraten

import random 

versuche = 0;
raten = True

zufallszahl = random.randint(1,100)
# print(zufallszahl)

while(raten):
    eingabe = input("Geben sie eine Zahl zwischen 1-100 ein. ")
    eingabe = int(eingabe)

    if(eingabe == zufallszahl):
        raten = False
    else:
        versuche = versuche + 1

print("Du hast es geschafft! Anzahl der Versuche: ", versuche + 1)
    
