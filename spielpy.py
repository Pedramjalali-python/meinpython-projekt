import random

class Spiel:
    spiel_optionen = ["papier", "schere", "stein"]

    def __init__(self):
        self.spiel_optionen = Spiel.spiel_optionen

    def computer_choice(self):
        return random.choice(self.spiel_optionen)

    def zeige_optionen(self):
        print("Verfügbare Optionen: papier, schere, stein")

    def command_eingabe(self):
        eingabe = input("Geben Sie Ihre Wahl (papier, schere, stein) ein: ").lower()
        if eingabe not in self.spiel_optionen:
            print("Ungültige Eingabe! Bitte wählen Sie papier, schere oder stein.")
            return None
        return eingabe
    
    def spiel_verlauf(self):
        self.zeige_optionen()
        while True:
            spieler_wahl = self.command_eingabe()
        
            computer_wahl = self.computer_choice()
            print(f"Der Computer wählt: {computer_wahl}")

            if spieler_wahl == computer_wahl:
                print("Unentschieden!")

            elif (spieler_wahl == "papier" and computer_wahl == "stein") or \
                 (spieler_wahl == "stein" and computer_wahl == "schere") or \
                 (spieler_wahl == "schere" and computer_wahl == "papier"):
                print("du hast gewonnen")
            else:
                print("computer gewonnen")


spiel = Spiel()
spiel.spiel_verlauf()
