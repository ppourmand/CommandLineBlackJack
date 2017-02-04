import random
import time
import os


class Deck:
    def __init__(self):
        self.reset_deck()

    def print_deck(self):
        for i in self.deck:
            i.print_card()

    def deal(self):
        # if there are cards left in the deck, pick one at random and return
        if len(self.deck) > 0:
            choice = random.choice(self.deck)
            self.deck.remove(choice)
        # if there are no more cards, reset and take a card at random
        else:
            self.reset_deck()
            choice = random.choice(self.deck)
            self.deck.remove(choice)

        return choice

    def reset_deck(self):
        self.deck = []
        suit_ticker = 0
        suit = 'default'
        for i in range(1, 56):
            if i % 14 != 0:
                if i <= 13:
                    suit = 'Diamond'
                elif i > 13 and i <= 27:
                    suit = 'Hearts'
                elif i > 27 and i <= 41:
                    suit = 'Clubs'
                else:
                    suit = 'Spades'
                my_card = Card(suit, i % 14)
                self.deck.append(my_card)


class Card:
    def __init__(self, suit, true_value):
        self.suit = suit
        self.true_value = true_value
        self.face_value = ''

        if true_value == 11:
            self.face_value = 'Jack'
            self.true_value = 10
        elif true_value == 12:
            self.face_value = 'Queen'
            self.true_value = 10
        elif true_value == 13:
            self.face_value = 'King'
            self.true_value = 10
        elif true_value == 1:
            self.face_value = 'Ace'
        else:
            self.face_value = str(true_value)

    def print_card(self):
        print(self.face_value + " of " + self.suit)

    def get_true_value(self):
        return self.true_value

class Player:
    def __init__(self):
        self.hand_value = 0
        self.hand = []

    def hit(self, card):
        self.hand.append(card)
        self.hand_value += card.get_true_value()

    def print_hand(self):
        for i in self.hand:
            i.print_card()

    def get_hand_value(self):
        return self.hand_value

class Game:
    def play(self):


        while 1:
            os.system('clear')
            print("=========================")
            print("= Welcome to Black Jack =")
            print("=========================")
            player_turn_over = False

            dealer = Player()
            deck = Deck()
            player = Player()

            # dealer gets 1 card
            d = deck.deal()
            dealer.hit(d)

            # you get two cards
            d = deck.deal()
            player.hit(d)
            d = deck.deal()
            player.hit(d)

            print("Dealer begins with:")
            dealer.print_hand()
            print("")

            print("Player start with:")
            player.print_hand()
            print("Total: ", end='')
            print(player.get_hand_value())

            while not player_turn_over:
                player_in = input("Hit? (Y/N) > ")

                if player_in.lower() == 'y':
                    # give a card to the player
                    c = deck.deal()
                    player.hit(c)

                    # tell him what it was, and what is currently in his hand
                    os.system('clear')


                    print("Card dealt: ", end='')
                    c.print_card()
                    print("Player hand:")
                    player.print_hand()
                    print("Total: ", end='')
                    print(player.get_hand_value())
                    print("\nDealer value:")
                    print(dealer.get_hand_value())

                    # if you get 21, your turn is over
                    if player.get_hand_value() == 21:
                        player_turn_over = True

                    # if you get more than 21, auto lose
                    if player.get_hand_value() > 21:
                        break
                else:
                    player_turn_over = True

            # dealer has to hit as long as < 17
            while dealer.get_hand_value() < 17 and player.get_hand_value() <= 21:
                d = deck.deal()
                dealer.hit(d)
                os.system('clear')
                print("Card dealt: ", end='')
                d.print_card()
                print("Dealers hand:")
                dealer.print_hand()
                print("Total: ", end='')
                print(dealer.get_hand_value())
                print("")
                time.sleep(2)

            os.system('clear')
            if player.get_hand_value() > 21:
                print("Player bust, dealer wins!")
            elif dealer.get_hand_value() > 21:
                print("Dealer bust, Player wins!")
            elif player.get_hand_value() > dealer.get_hand_value() and dealer.get_hand_value() != 21:
                print("Player wins!")
            else:
                print("Dealer wins!")

            print("Dealers hand:")
            dealer.print_hand()
            print("Total: ", end='')
            print(dealer.get_hand_value())

            print("\nPlayer hand:")
            player.print_hand()
            print("Total: ", end='')
            print(player.get_hand_value())

            answer = input("Play again? (y/n): ")

            if answer.lower() != 'y':
                return



g = Game()
g.play()
