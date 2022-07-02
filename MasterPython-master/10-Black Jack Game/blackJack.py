import random
suits = ('Hearts','Diamonds','Spades','Clubs')
ranks = ('Two','Three','Four','Five','Six','Seven','Eight','Nine','Ten','Jack','Queen','King','Ace')
values = {'Two':2,'Three':3,'Four':4,'Five':5,'Six':6,'Seven':7,'Eight':8,'Nine':9,'Ten':10,'Jack':10,'Queen':10,'King':10,'Ace':11}
playing = True

class Card():

    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return self.rank+ " of "+self.suit

class Deck():
    def __init__(self):
        self.deck = [] # start with an empty list
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit,rank))
    def __str__(self):
        deck_comp = ''
        for card in self.deck:
            deck_comp += '\n'+ card.__str__()
        return "The deck has: " +deck_comp

    def shufle(self):
        random.shuffle(self.deck)

    def deal(self):
        single_card = self.deck.pop()
        return single_card

class Hand():
    def __init__(self):
        self.cards = [] # start with an empty list as we did in Deck class
        self.value = 0 # Start with zero value
        self.aces = 0 # add an attribute to help track of aces

    def add_card(self,card):
        #card passed in from Deck.deal() --> single_card(suit,rank)
        self.cards.append(card)
        self.value += values[card.rank]

        #Track aces
        if card.rank == 'Ace':
            self.aces  += 1


    def adjust_for_ace(self):
        #If total value > 21 and you still have an ace
        # then change my value to 1 instead of 11
        while self.value > 21 and self.aces > 0:
            self.value -= 10
            self.aces -= 1

class Chips():

    def __init__(self):
        self.total = 100 # this can be set to a default value
        self.bet = 0

    def win_bet(self):
        self.total += self.bet

    def lose_bet(self):
        self.total -= self.bet

def take_bet(chips):
    while True:

        try:
            chips.bet = int(input("How many chips would you like to bet?  "))
        except:
            print("Sorry!! please provide an integer")
        else:
            if chips.bet > chips.total:
                print("sorry!! you do not have enough chips, you have {}".format(chips.total))
            else:
                break


def hit(deck,hand):
    single_card = deck.deal()
    hand.add_card(single_card)
    hand.adjust_for_ace()

def hit_or_stand(deck,hand):
    global playing
    while True:
        x = input("Hit or Stand? Enter 'h' for Hit and 's' for Stand")

        if x[0].lower() == 'h':
            hit(deck,hand)
        elif x[0].lower() == 's':
            print("Player Stands, Dealr's turn")
            playing = False
        else:
            print("Sorry, I could not understand, please enter h or s only!")
            continue
        break

def show_some(player,dealer):
    print("DEALERS HAND:")
    print("one card hidden!")
    print("\n")
    print("PLAYERS HAND:")
    for card in player.cards:
        print(card)

def show_all(player,dealer):
    print("DEALERS HAND:")
    for card in dealer.cards:
        print(card)
    print("\n")
    print("PLAYERS HAND:")
    for card in player.cards:
        print(card)



def player_busts(player,dealer,chips):
    print("BUST PLAYER!")
    chips.lose_bet()

def player_wins(player,dealer,chips):
    print("PLAYER WINS!")
    chips.win_bet()

def dealer_busts(player,dealer,chips):
    print("PLAYER WINS! DEALER BUSTED")
    chips.win_bet()

def dealer_wins(player,dealer,chips):
    print("DEALER WINS!")
    chips.lose_bet()

def push(player,dealer):
    print("Play and Dealer tie!! PUSH")

#####Logic of the GAME###########
while True:
    # Print an opening statement
    print("WELCOME TO BLACKJACK")
    # Create and shuffle the deck, deal two cards to each player
    deck = Deck()
    deck.shufle()

    player_hand = Hand()
    player_hand.add_card(deck.deal())
    player_hand.add_card(deck.deal())

    dealer_hand = Hand()
    dealer_hand.add_card(deck.deal())
    dealer_hand.add_card(deck.deal())

    # set up player's chip
    player_chips = Chips()

    #prompt the player for their bet
    take_bet(player_chips)
    # Show cards but keep one dealer card hidden
    show_some(player_hand,dealer_hand)

    while playing: # recall this variable from our hit_or_stand function

        # prompt player to Hit or Stand
        hit_or_stand(deck,player_hand)

        #show cards but keep dealers card hidden
        show_some(player_hand, dealer_hand)

        if player_hand.value > 21:
            player_busts(player_hand, dealer_hand,player_chips)

            break
    if player_hand.value <= 21:
        while dealer_hand.value < 17:
            hit(deck,dealer_hand)

        show_all(player_hand,dealer_hand)

        if dealer_hand.value > 21:
            dealer_busts(player_hand,dealer_hand,player_chips)
        elif dealer_hand.value > player_hand.value:
            dealer_wins(player_hand,dealer_hand,player_chips)
        elif dealer_hand.value < player_hand.value:
            player_wins(player_hand, dealer_hand, player_chips)
        else:
            push(player_hand, dealer_hand)
    # inform players of their total chips
    print("\n Player total chips are at : {}".format(player_chips.total))
    # Ask players to play again
    new_game = input("Would you like to play another hand? y/n   ")

    if new_game[0].lower() == 'y':
        playing = True
        continue
    else:
        print("Thank you for playing")

        break

#test_deck = Deck()
#test_deck.shufle()
#player
#test_player = Hand()
#Deal 1 card from deck Card(suit,rank)
#pulled_card = test_deck.deal()
#print(pulled_card)
#test_player.add_card(pulled_card)
#print(test_player.value)
