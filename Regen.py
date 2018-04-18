# Regen.py

regen = True

eingabe1 = input("Hast du einen Regenschirm? Ja oder nein. ")

if(eingabe1 == "ja"):
    print("Gut das du einen Schirm dabei hast. Geh jetzt nach draußen")
    regen = False

while(regen):
    print("Warte bis der Regen aufhört... ")
    eingabe = input("Regnet es noch?")

    if (eingabe == "nein"):
        regen = False
    elif (eingabe == "ja"):
        print("Es regnet noch immer... ")
    else:
        print ("bitte nur ja oder nein eingeben")
    print("Jetzt regnet es nicht mehr ")