print("Hallo ich bin ein Laptop")
name = input("Wie ist dein Name?")
print("Schön dich zu treffen ", name ,". Dein Name ist ", len(name) ,"Zeichen lang")

print("Noch eine Frage. ")
alter = input("Wie alt bist du den? ") 
alter = int(alter)
if(alter > 100):
    print("Das ist wohl ein Scherz - oder? ")
else:
    print("Aha, sehr interressant ", name, " du wirst in einem Jahr ", alter+1, " Jahre alt sein.")
print("Tschüssi...")
