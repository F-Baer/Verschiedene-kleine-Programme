
def daten_lager():
    daten = {}
    return daten   

def auswahl():
    lager = daten_lager()

    gelungen = False
    while not gelungen:
        try:            
            print("\nWilkommen bei ihrer Lagerverwaltung")
            print("was möchten sie tun?\n")
            print("1 - Eingabe einer neuen Kiste.")
            print("2 - Löschen der Daten einer vorhandenen Kiste.")
            print("3 - Ändern der Daten einer vorhandenen Kiste.")
            print("4 - Anzeigen der Daten einer Vorhandenen Kiste.")
            print("5 - Anzeigen der Daten aller vorhandenen Kisten.")
            print("6 - Beenden.")
        
            eingabe = int(input("\nEingabe: "))    
          
            if eingabe == 1:
                neue_kiste(lager)
            elif eingabe == 2:
                loeschen(lager)
            elif eingabe == 3:
                aendern(lager)
            elif eingabe == 4:
                anzeigen(lager)
            elif eingabe == 5:
                anzeigen_alle(lager)
            elif eingabe == 6:
                print("Programm wird beendet.")
                gelungen = True
            else:
                print("Sie haben eine falsche Auswahl getroffen")
        except ValueError:
            print("Sie haben eine falsche Auswahl getroffen.")
              
def neue_kiste(lager):  
    
    if not lager:
        kisten_nummer = 1
    else: 
        kisten_nummer = max(lager.keys()) + 1             
        
    breite = float(input("Bitte geben sie die Breite der Kiste ein: "))
    laenge = float(input("Bitte geben sie die Länge der Kiste ein: "))
    hoehe = float(input("Bitte geben sie die Höhe der Kiste ein: "))
    
    lager[kisten_nummer] = [breite, laenge, hoehe]
    print("Die Kiste wurde erfolgreich hinzugefügt.")
    
def loeschen(lager):    
    if not lager:
        print("Kein Datensatz gefunden.")
    else:    
        print("Folgende Kisten sind angelegt\n")
        for daten in lager:       
            print("Kiste", daten)  
             
        eingabe = int(input("\nBitte geben sie die Kistennummer ein die sie löschen wollen. "))
        
        if eingabe in lager:
            del lager [eingabe]
            print("Der Eintrag wurde erfolgreich gelöscht.")
        else: 
            print("Diese Kistenummer existiert nicht.")
    
def aendern(lager):    
    if not lager:
        print("Kein Datensatz gefunden.")
    else:    
        print("Folgende Kisten sind angelegt\n")
        for daten in lager:       
            print("Kiste", daten)  
    
        eingabe = int(input("\nBitte geben sie die Kistennummer ein die sie ändern wollen. ")) 
        
        if eingabe in lager:
            breite = float(input("Bitte geben sie die Breite der Kiste ein: "))
            laenge = float(input("Bitte geben sie die Länge der Kiste ein: "))
            hoehe = float(input("Bitte geben sie die Höhe der Kiste ein: "))  
            lager[eingabe] = [breite, laenge, hoehe]    
            print("Der Eintrag wurde erfolgreich geändert.")
        else:
            print("Diese Kistenummer existiert nicht.")
    
def anzeigen(lager):
    if not lager:
        print("Kein Datensatz gefunden.")
    else:    
        print("Folgende Kisten sind angelegt\n")
        for daten in lager:       
            print("Kiste", daten)  
   
        eingabe = int(input("\nBitte geben sie die Kistennummer ein die sie einsehen wollen. "))
        if eingabe in lager: 
            daten = lager[eingabe]
            print("Breite:", daten[0], "Länge:", daten[1], "Höhe:", daten[2])
            
        else:
            print("Diese Kistenummer existiert nicht")
    
def anzeigen_alle(lager):
    if not lager:
        print("Kein Datensatz gefunden.")
    else:    
        print("Folgende Kisten sind angelegt\n")
        for kiste, daten in lager.items():        
            print("Kiste", kiste, "Breite:", daten[0], "Länge:", daten[1], "Höhe:", daten[2])

#Start des Programms
auswahl()