import random 
userIn = True
computerIn = True


cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10,
        2, 3, 4, 5, 6, 7, 8, 9, 10, 10,
        2, 3, 4, 5, 6, 7, 8, 9, 10, 10,
        2, 3, 4, 5, 6, 7, 8, 9, 10, 10,
        'J' ,'K', 'Q', 'A',
        'J' ,'K', 'Q', 'A',
        'J' ,'K', 'Q', 'A', 
        'J' ,'K', 'Q', 'A'
]

user = []
computer = []

def dealCard(turn):
    card = random.choice(cards)
    turn.append(card)
    cards.remove(card)


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



def revealComputer ():
    if len(user) == 2:
        return computer[0]
    elif len(computer) > 2:
        return computer[0], computer[1]



for _ in range(2):
    dealCard(computer)
    dealCard(user)


while userIn and computerIn:
    print("Hallo und Herzlich Wilkommen zum Blackjack!")
    u = input("möchten sie spielen?\n1 -> Ja\n2 -> Nein\nAntwort: ")
    if u == "1" or u == "j" or u == "J" or u == "ja" or u == "Ja" or u == "JA":   
        print(f"der Computer hat: {revealComputer()} und X")
        print(f"Sie haben {user} für insgesamt {total(user)}")
        if userIn:
            stayOrHit = input("1 -> hit\n2 -> Stay\n")
        if total(computer) > 16:
            computerIn = False
        else:
            dealCard(computer)
        if stayOrHit == "2":
            userIn = False
        else:
            dealCard(user)
        if total(user) >= 21:    
            break
        elif total(computer) >= 21:
            break

        if total(user) == 21:
            print(f"\nSie haben {total(user)} und den Computer hat {total(computer)}")
            print("Blackjack! Sie haben gewonnen!")
        elif total(computer) == 21:
            print(f"\nSie haben {total(user)} und den Computer hat {total(computer)}")
            print("Blackjack! der Computer hat gewonnen!")
        elif total(user) > 21:
            print(f"\nSie haben {total(user)} und den Computer hat {total(computer)}")
            print("Sie sind besiegt! computer hat gewonnen")
        elif total(computer) > 21:
            print(f"\nSie haben {total(user)} und den Computer hat {total(computer)}")
            print("Computer zerquetscht! Sie haben gewonnen!")
        elif 21 - total(computer) < 21 - total(user):
            print(f"\nSie haben {total(user)} und den Computer hat {total(computer)}")
            print("Computer hat gewonnen!")
        elif 21 - total(computer) > 21 - total(user):
            print(f"\nSie haben {total(user)} und den Computer hat {total(computer)}")
            print("Sie haben gewonnen!")
    elif u == "2" or u == "n" or u == "N" or u == "nein" or u == "Nein" or u == "NEIN":
        print("Schade! Schönnen Tag noch.")
        userIn = False
        computerIn = False
