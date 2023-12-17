import random
import os

logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""

def deal_cards():
    """Returns a random """
    return random.choice(cards)
def calculate_score(card):
    """Takes a list of cards and return the sum of those cards according blackJack"""
    if sum(card) == 21 and len(card) == 2:
        return 0
    if 11 in card and sum(card) > 21:
        # index = card[11]
        # card[index] = 1
        card.remove(11)
        card.append(1)
    return sum(card)

def compare(user,comp):
    if user == comp:
        return "Draw"
    elif user == 0:
        return "Win with a BLACKJACK"
    elif comp == 0:
        return "Opponent win with a BLACKJACK"
    elif user > 21:
        return "You went over.Opponent win."
    elif comp > 21:
        return "Opponent went over.You win"
    elif user > comp:
        return "You won"
    else:
        return "You lose"

cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
def playGame():
    print(logo)
    gameOver = False

    user_cards = []
    comp_cards = []
    for i in range(2):
        user_cards.append(deal_cards())
        comp_cards.append(deal_cards())
    while not gameOver:
        user_score = calculate_score(user_cards)
        comp_score = calculate_score(comp_cards)

        print(f"Your cards : {user_cards} , Score : {calculate_score(user_cards)}")
        print(f"Computer card : {comp_cards[0]}")

        if user_score == 0 or comp_score == 0 or user_score > 21:
            gameOver = True
        else:
            choice = input("enter 'y' to draw another card otherwise 'n' to stop the game : ").lower()
            if choice == 'y':
                user_cards.append(random.choice(cards))
            else:
                gameOver = True
    while comp_cards != 0 and comp_score < 17:
        comp_cards.append(random.choice(cards))
        comp_score = calculate_score(comp_cards)
    print(f"Your final hand : {user_cards}\tScore : {user_score}")
    print(f"Opponent's final hand : {comp_cards}\tScore : {comp_score}")
    print(compare(user=user_score,comp=comp_score))
playGame()
while input("Do you want to restart the game ?\nEnter 'y' for yes and 'n' for no : ") == 'y':
    os.system('cls')
    playGame()
print("Exting game...")