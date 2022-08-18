import random

spieler = True
computer = True


cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10,
        2, 3, 4, 5, 6, 7, 8, 9, 10, 10,
        2, 3, 4, 5, 6, 7, 8, 9, 10, 10,
        2, 3, 4, 5, 6, 7, 8, 9, 10, 10,
        'J' ,'K', 'Q', 'A',
        'J' ,'K', 'Q', 'A',
        'J' ,'K', 'Q', 'A', 
        'J' ,'K', 'Q', 'A'
]


SPIELER = []
COMPUTER = []



# Diese Funktion wählt eine zufällige Karte aus, 
# fügt dem Argument der Funktionsaufrufe turn 
# hinzu und entfernt sie aus der Liste der Karten, 
# damit sie nicht noch einmal verwendet wird
def dealCard(turn):
    card = random.choice(cards)
    turn.append(card)
    cards.remove(card)





# Diese Funktion hat ein Argument namens turn, 
# erstellt eine Variable namens total und ein Array namens face. 
# und macht die Logik hinter den J-, K- und Q-Karten, die im echten 
# Blackjack-Kartenspiel existieren
def total(turn):
    total = 0
    face = ['J', 'K', 'Q']
    for card in turn:
        if card in range(1, 11):
            total += card
        elif card in face:
            total += 1
        else:
            if total > 11:
                total += 10
            else:
                total += 11
    return total   



spielerTotal = total(SPIELER)
computerTotal = total(COMPUTER)



def revealComputer():
    if spielerTotal == 2:
        return COMPUTER[0]
    elif computerTotal > 2:
        return COMPUTER[0], COMPUTER[1]



# Diese For-Schleife veranlasst sowohl den Spieler
# als auch den Computer, zufällige Karten mit der Funktion 
# dealCard zu erhalten, und ruft das Argument als Spieler und Computer auf
for _ in range(2):
    dealCard(COMPUTER)
    dealCard(SPIELER)







while spieler and computer:
    print("* * * Hallo und Herzlich Wilkommen zum Blackjack! * * *")
    u = input("möchten sie spielen?\n1 -> Ja\n2 -> Nein\nAntwort: ")
    if u == "1" or u == "j" or u == "J" or u == "ja" or u == "Ja" or u == "JA":   
        print(f"der Computer hat: {revealComputer()} und X")
        print(f"Sie haben {SPIELER} für insgesamt {spielerTotal}")
        if spieler:
            stayOrHit = input("1 -> hit\n2 -> Stay\n")
        if computerTotal > 16:
            computer = False
        else:
            dealCard(COMPUTER)
        if stayOrHit == "2":
            spieler = False
        else:
            dealCard(SPIELER)
        if spielerTotal >= 21:    
            break
        elif computerTotal >= 21:
            break

        if spielerTotal == 21:
            print(f"\nSie haben {spielerTotal} und den Computer hat {computerTotal}")
            print("Blackjack! Sie haben gewonnen!")
        elif computerTotal== 21:
            print(f"\nSie haben {spielerTotal} und den Computer hat {computerTotal}")
            print("Blackjack! der Computer hat gewonnen!")
        elif spielerTotal > 21:
            print(f"\nSie haben {spielerTotal} und den Computer hat {computerTotal}")
            print("Sie sind besiegt! computer hat gewonnen")
        elif computerTotal > 21:
            print(f"\nSie haben {spielerTotal} und den Computer hat {computerTotal}")
            print("Computer zerquetscht! Sie haben gewonnen!")
        elif 21 - computerTotal < 21 - spielerTotal:
            print(f"\nSie haben {spielerTotal} und den Computer hat {computerTotal}")
            print("Computer hat gewonnen!")
        elif 21 - computerTotal > 21 - spielerTotal:
            print(f"\nSie haben {spielerTotal} und den Computer hat {computerTotal}")
            print("Sie haben gewonnen!")
    elif u == "2" or u == "n" or u == "N" or u == "nein" or u == "Nein" or u == "NEIN":
        print("Schade! Schönnen Tag noch.")
        spieler = False
        computer = False
