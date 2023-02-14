
import random


def draw():
    global card_deck
    idx = random.randint(0, len(card_deck) - 1)
    return card_deck.pop(idx)

def hand_value(deck):
    hand_value = 0
    aces = 0
    for card in deck:  
        temp = card[1:]
        if str(temp).isdecimal():
             hand_value += int(card[1:])
        elif card[1:] != "A":
            hand_value +=10
        else:
            aces += 1
            hand_value += 11
    while hand_value > 21 and aces > 0:
        hand_value -= 10
        aces -= 1
    return hand_value

def reset_game():
    global player_hand
    global dealer_hand
    global card_deck
    player_hand = []
    dealer_hand = []
    card_deck = ["D2","H2","C2","S2","D3","H3","C3","S3","D4","H4","C4","S4","D5","H5","C5","S5","D6","H6","C6","S6","D7","H7","C7","S7","D8","H8","C8","S8","D9","H9","C9","S9","D10","H10","C10","S10","DJ","HJ","CJ","SJ","DD","HD","CD","SD","DK","HK","CK","SK","DA","HA","CA","SA"]

def check_blackjack(deck):
    return hand_value(deck) == 21

def check_busted(deck):
    return hand_value(deck) > 21

def replay():
    print("replay? [y/n]")
    user_input = input()
    if user_input == "y":
        play_game()
    else:
        print("bye!")
        exit(0)

def play(user_hand):
    while True:
        print(f"Dealer: {dealer_hand[0]}\nPlayer: {user_hand}\n\n(d)raw\n(s)tand")
        user_input = input()
        if user_input == "d":
            user_hand.append(draw())
            if check_busted(user_hand):
                return user_hand
        elif user_input == "s":
            return user_hand

def play_dealer(hand):
    while hand_value(hand) < 17:
        hand.append(draw)
    return hand

def play_game():
    reset_game()
    player_hand.append(draw())
    dealer_hand.append(draw())
    player_hand.append(draw())
    dealer_hand.append(draw())

    if check_blackjack((player_hand)) and check_blackjack(dealer_hand):
        print(f"Dealer: {dealer_hand}\nPlayer: {player_hand}")
        print("natural draw")
        replay()
    elif check_blackjack(player_hand):
        print(f"Dealer: {dealer_hand}\nPlayer: {player_hand}")
        print("Blackjack! You won!")
        replay()
    elif check_blackjack(dealer_hand):
        print(f"Dealer: {dealer_hand}\nPlayer: {player_hand}")
        print("Blackjack! You lost!")
        replay()

    if player_hand[0][1:] == player_hand[1][1:]:
        print(f"Dealer: {dealer_hand[0]}\nPlayer: {player_hand}")
        print("split? [y/n]")
        if input() == "y":
            player_hand2 = [player_hand.pop(1)]
            player_hand.append(draw())
            player_hand2.append(draw())
            play(player_hand)
            if check_busted(player_hand):
                print("Bust!")
            play(player_hand2)
            if check_busted(player_hand2):
                print("Bust!")
            if check_busted(player_hand) and check_busted(player_hand2):
                print(f"Dealer: {dealer_hand}\nPlayer: {player_hand}\n        {player_hand2}")
                print("Busted both hands! You lost!")
                replay()
            play_dealer(dealer_hand)
            if check_busted(dealer_hand):
                print("Bust! You won!")
                print(f"Dealer: {dealer_hand}\nPlayer: {player_hand}\n        {player_hand2}")
                replay()
            elif (hand_value(player_hand) or hand_value(player_hand2)) > hand_value(dealer_hand):
                print("You won!")
                print(f"Dealer: {dealer_hand}\nPlayer: {player_hand}\n        {player_hand2}")
                replay()
            elif (hand_value(player_hand) and hand_value(player_hand2)) < hand_value(dealer_hand):
                print(f"Dealer: {dealer_hand}\nPlayer: {player_hand}\n        {player_hand2}")
                print("You lost!")
                replay()
            else:
                print(f"Dealer: {dealer_hand}\nPlayer: {player_hand}\n        {player_hand2}")
                print("Draw!")
                replay()

    play(player_hand)
    if check_busted(player_hand):
        print("Bust!")
        replay()
    print(dealer_hand)
    play_dealer(dealer_hand)
    if check_busted(dealer_hand):
        print(f"Dealer: {dealer_hand}\nPlayer: {player_hand}")
        print("Bust! You won!")
        replay()
    elif hand_value(player_hand) > hand_value(dealer_hand):
        print(f"Dealer: {dealer_hand}\nPlayer: {player_hand}")
        print("You won!")
        replay()
    elif hand_value(player_hand) < hand_value(dealer_hand):
        print(f"Dealer: {dealer_hand}\nPlayer: {player_hand}")
        print("You lost!")
        replay()
    else:
        print(f"Dealer: {dealer_hand}\nPlayer: {player_hand}")
        print("Draw!")
        replay()


card_deck = []
player_hand = []
dealer_hand = []

if __name__ == "__main__":
    play_game()

