import random

user = True
computer = True
USER = []
COMPUTER = []

cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10,
        2, 3, 4, 5, 6, 7, 8, 9, 10, 10,
        2, 3, 4, 5, 6, 7, 8, 9, 10, 10,
        2, 3, 4, 5, 6, 7, 8, 9, 10, 10,
        'J' ,'K', 'Q', 'A',
        'J' ,'K', 'Q', 'A',
        'J' ,'K', 'Q', 'A', 
        'J' ,'K', 'Q', 'A'
]


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


userTotal = total(USER)
computerTotal = total(COMPUTER)



def revealComputer():
    if userTotal == 2:
        return COMPUTER[0]
    elif computerTotal > 2:
        return COMPUTER[0], COMPUTER[1]


for _ in range(2):
    dealCard(COMPUTER)
    dealCard(USER)



while user and computer:
    print("* * * Hello and welcome to blackjack! * * *")
    requiredAnswer = input("Do you want to play?\n1 -> Yes\n2 -> Mp\Answer: ")
    if requiredAnswer == "1" or requiredAnswer == "j" or requiredAnswer == "J" or requiredAnswer == "ja" or requiredAnswer == "Ja" or requiredAnswer == "JA":   
        print(f"the computer has: {revealComputer()} and X")
        print(f"You have {USER} for a total of {userTotal}")
        if user:
            stayOrHit = input("1 -> hit\n2 -> Stay\n")
        if computerTotal > 16:
            computer = False
        else:
            dealCard(COMPUTER)
        if stayOrHit == "2":
            user = False
        else:
            dealCard(USER)
        if userTotal >= 21:    
            break
        elif computerTotal >= 21:
            break

        if userTotal == 21:
            print(f"\You have {userTotal} and the Computer has {computerTotal}")
            print("Blackjack! You win!")
        elif computerTotal== 21:
            print(f"\You have {userTotal} and the Computer has {computerTotal}")
            print("Blackjack! The Computer win!")
        elif userTotal > 21:
            print(f"\You have {userTotal} and the Computer has {computerTotal}")
            print("You are defeated! The computer win")
        elif computerTotal > 21:
            print(f"\nSie haben {userTotal} und den Computer has {computerTotal}")
            print("computer crushed! You win!")
        elif 21 - computerTotal < 21 - userTotal:
            print(f"\nYou have {userTotal} and the Computer has {computerTotal}")
            print("The Computer Win!")
        elif 21 - computerTotal > 21 - userTotal:
            print(f"\You have {userTotal} and the Computer has {computerTotal}")
            print("You win!")
    elif requiredAnswer == "2" or requiredAnswer == "n" or requiredAnswer == "N" or requiredAnswer == "no" or requiredAnswer == "No" or requiredAnswer == "NO":
        print("What a shame! Have a good time.")
        user = False
        computer = False
