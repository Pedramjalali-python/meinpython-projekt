class Rechner:
    def __init__(self):
        self.rechner_optionen = ["1: multiply", 
                                "2: addieren", 
                                "3: dividieren",
                                "4: subtrahieren"]
        
    def option_zeigen(self):
        for option in self.rechner_optionen:
            print(option)

    def multiply(self):
        eingabe = int(input("erste zahl eingeben: "))
        eingabe_2 = int(input("zweite zahl eingeben: "))
        ergebniss = eingabe * eingabe_2
        print(f"ergebniss ist: {ergebniss}")
        return ergebniss
    
    
    def addieren(self):
        eingabe_1 = int(input("erste zahl eingeben"))
        eingabe_2 = int(input("zweite zahl eingeben: "))
        ergebniss = eingabe_1 + eingabe_2
        print(f"ergebniss ist: {ergebniss}")
        return ergebniss
    
    def dividiren(self):
        eingabe_1 = int(input("erste zahl eingeben: "))
        eingabe_2 = int(input("zweite zahl eingeben: "))
        ergebniss = eingabe_1 // eingabe_2
        print(f"ergebniss ist: {ergebniss}")
        return ergebniss
    
    def subtrahieren(self):
        eingabe_1 = int(input("erste zahl eingeben: "))
        eingabe_2 = int(input("zweite zahl eingeben: "))
        ergebniss = eingabe_1 - eingabe_2
        print(f"ergebniss ist: {ergebniss}")
        return ergebniss
    
    def choice(self):
        while True:
            self.option_zeigen()
            choice = int(input("choice your option: "))
            if choice == 1:
                self.multiply()
            elif choice == 2:
                self.addieren()
            elif choice == 3:
                self.dividiren()
            elif choice == 4:
                self.subtrahieren()
            else:
                print("keine option mehr")

Re = Rechner()
Re.choice()
