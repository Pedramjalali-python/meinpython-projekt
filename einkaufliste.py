class Markt:
    def __init__(self):
        self.produkte = ["1: laptops", "2: keleidungen", "3: books", "4: parfüme"]
        self.einkaufliste = []

    def laptops_marke(self):
        return ["1: lenovo", "2: asus", "3: hp",]

    def kleidungen(self):
        return ["1: tschirt", "2: socke", "3: hose"]
    
    def books(self):
        return ["1: die Liebe", "2: sicher_B2", "3: Irans Geschischte"]
    
    def parfume(self):
        return ["1: victoria", "2: blue channel", "3: tom ford"]
        
    def zeige_produkte(self):
        print("Produkte:")
        for produkt in self.produkte:
            print(produkt)

    def zeige_einkaufliste(self):
        if not self.einkaufliste:
            print("die einkaufliste ist leer")
        else:
            print("einkaufliste: ")
            for produkte in self.einkaufliste:
                print(produkte)


    def benutzer_eingabe(self):
        self.zeige_produkte()

        while True:
        
            try:
                eingabe = int(input("Geben Sie eine Zahl ein (oder 0 zum Beenden): "))
                
                if eingabe == 0:
                    print("Programm beendet.")
                    break
                
                elif eingabe == 1:
                    print("Laptops:")
                    marken = self.laptops_marke()
                    for marke in marken:
                        print(marke)
                    marke_auswahl = int(input("model auswahl: "))
                    if marke_auswahl == 1 or marke_auswahl == 2 or marke_auswahl == 3:
                        self.einkaufliste.append(marken[marke_auswahl - 1])
                        print(f"{marken[marke_auswahl - 1]} zur Liste hinzugefügt")

                    else:
                        print("Ungültige Auswahl.")

                elif eingabe == 2:
                    print("Kleidungen:")
                    kleidungen = self.kleidungen()
                    for kleidung in kleidungen:
                        print(kleidung)
                    kleidung_auswahl = int(input("kleidung auswählen: "))
                    if kleidung_auswahl == 1 or kleidung_auswahl == 2 or kleidung_auswahl == 3:
                        self.einkaufliste.append(kleidungen[kleidung_auswahl - 1])
                        print(f"{kleidungen[kleidung_auswahl - 1]} zur Liste hinzugefügt")
                   
                elif eingabe == 3:
                    print("Bücher:")
                    books = self.books()
                    for book in books:
                        print(book)
                    book_auswahl = int(input("book auswälen: "))
                    if book_auswahl == 1 or book_auswahl == 2 or book_auswahl == 3:
                        self.einkaufliste.append(books[book_auswahl - 1])
                        print(f"{books[book_auswahl - 1]} zur Liste hinzugefügt")
                    
                elif eingabe == 4:
                    print("Parfüme:")
                    parfume = self.parfume()
                    for parfum in parfume:
                        print(parfum)
                    parfum_auswahl = int(input("parfum auswählen: "))
                    if parfum_auswahl == 1 or parfum_auswahl == 2 or parfum_auswahl == 3:
                        self.einkaufliste.append(parfume[parfum_auswahl - 1])
                        print(f"{parfume[parfum_auswahl - 1]} zur liste hinzugefügt")

                      
                else:
                    print("keine produkte mehr!")

            except ValueError:
                print("bitte geben sie eine gültige zahl ein!: ")

        
        self.zeige_einkaufliste()
            

ma = Markt()
ma.benutzer_eingabe()
