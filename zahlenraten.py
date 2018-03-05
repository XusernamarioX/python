#zahlenraten

import random
zufallszahl = (random.randint(1,10))

titel = "Willkommen beim Zahenraten!"
von = int(intput("Bitte die Zufallszahl-Unterschranke festlegen: "))
bis = int(input("Bitte die Zufallszahl-Oberschranke festlegen: "))
text = "Bitte versuche meine Zahl zwischen ", von , " und ", bis, " zu erraten!"
zufallszahl = (random.randint(von,bis))
eingabeText = "Bitte eine Zahl eingeben: "

print(text)
print(text)
fertig = False
anzahlderversuche = 0

while fertig  == False:
    anzahlderversuche = anzahlderversuche+1
    zahl = int (input(eingabeText))
    if(zahl == zufallszahl):
        print("Gewonnen!")
        fertig = True
    elif(zahl < zufallszahl):
        print("Die Zahl ist größer!")
    else:
        print("Die Zahl ist kleiner")


print("Super, du hast dafür ", anzahlderversuche, " Versuche benötigt")
print("Ende!")
