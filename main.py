import random

def create_deck():
    suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
    values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    deck = [(suit, value) for suit in suits for value in values]
    random.shuffle(deck)
    return deck

def deal_card(deck):
    return deck.pop()

def calculate_hand_value(hand):
    value = 0
    num_aces = 0
    for card in hand:
        if card[1] in 'JQK':
            value += 10
        elif card[1] == 'A':
            num_aces += 1
            value += 11
        else:
            value += int(card[1])
    while value > 21 and num_aces:
        value -= 10
        num_aces -= 1
    return value

def get_bet(balance):
    while True:
        try:
            bet = float(input(f"You have ${balance:.2f}. How much would you like to bet? "))
            if 0 < bet <= balance:
                return bet
            else:
                print("Invalid bet amount. It must be more than $0 and no more than your balance.")
        except ValueError:
            print("Please enter a valid number.")

def play_blackjack():
    balance = 5.00  # Initial player balance
    deck = create_deck()
    continue_playing = True

    while continue_playing and balance > 0:
        bet = get_bet(balance)
        balance -= bet
        
        player_hand = [deal_card(deck), deal_card(deck)]
        dealer_hand = [deal_card(deck), deal_card(deck)]

        player_turn = True
        while player_turn:
            print("Your hand:", player_hand, "Value:", calculate_hand_value(player_hand))
            if calculate_hand_value(player_hand) > 21:
                print("You bust! Dealer wins.")
                break
            action = input("Do you want to 'hit' or 'stand'? ")
            if action.lower() == 'hit':
                player_hand.append(deal_card(deck))
            else:
                player_turn = False

        if calculate_hand_value(player_hand) <= 21:
            while calculate_hand_value(dealer_hand) < 17:
                dealer_hand.append(deal_card(deck))

            print("Dealer's hand:", dealer_hand, "Value:", calculate_hand_value(dealer_hand))
            if calculate_hand_value(dealer_hand) > 21 or calculate_hand_value(player_hand) > calculate_hand_value(dealer_hand):
                print("You win!")
                balance += bet * 2
            elif calculate_hand_value(player_hand) == calculate_hand_value(dealer_hand):
                print("It's a draw!")
                balance += bet
            else:
                print("Dealer wins!")

        print(f"Your current balance is: ${balance:.2f}")
        if balance <= 0:
            print("You've run out of money!")
            continue_playing = False
        else:
            continue_playing = input("Do you want to play another hand? (yes/no) ").lower() == 'yes'

        if len(deck) < 10:
            deck = create_deck()  # Re-shuffle and recreate the deck if low on cards

if __name__ == "__main__":
    play_blackjack()
