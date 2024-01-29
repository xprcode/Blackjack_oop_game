"""
Blackjack Game Module

This module defines the 'Game' class, which represents a simple text-based Blackjack game.
The game utilizes the 'Deck' and 'User' classes
from external modules for managing the deck of cards and users.

Classes:
    - Game: Manages the flow and logic of the Blackjack game.

    External Dependencies:
    - 'Deck' class from the 'deck' module.
    - 'User' class from the 'user' module.
"""

from deck import Deck
from user import User

BLACKJACK_SCORE = 21

class Game:
    """
    Game: Manages the flow and logic of the Blackjack game.
    """
    def __init__(self) -> None:
        self.game_deck = Deck()
        self.game_deck.shuffle()
        self.player = User()
        self.croupier = User()

    @staticmethod
    def _print_menu():
        """
        Print the game menu with player decision options.
        """
        print('________' * 10)
        print('Please type what would you like to do?\n')
        print('next - get the next card from the deck')
        print('pass - finish the round\n')


    def _print_both_results(self):
        """
        Print player and croupier score.
        """
        print('________' * 10)
        print('\nYour cards: ')
        print(f'{self.player}\n')
        print('Croupier cards: ')
        print(f'{self.croupier}\n')


    @staticmethod
    def decision_validator():
        """
        Checking the string given by player if he wants to get another card or pass.

        Returns:
            boolean: Next - True to get next card and continue while loop.
                     Pass - False to break the loop and give the game to the croupier. 
        """
       
        while True:
            text = input('Do you want to get next card or pass? (next/pass)\n').lower()
            try:
                if text.strip() == 'next':
                    return True
                if text.strip() == 'pass':
                    return False

                print('Invalid input. Please enter either "next" or "pass".')

            except ValueError:
                print('Invalid input. Please enter either "next" or "pass".')

    def start_to_play(self):
        """
        Initiates the Blackjack game, allowing the player to get two first cards.
        """
        for _ in range(2):
            self.player.player_cards.append(self.game_deck.card_taking())
        self.player.player_score_count()

        print('\nYour cards: ')
        print(f'{self.player}\n')


    def mid_end_game(self):
        """
        Manages the player's turn in the Blackjack game.
        Allows the player to draw cards or pass, updating the score and game reulst. 
        """
        # Player decision and play loop till the score is lower or equel than 21. 
        while self.player.player_score < BLACKJACK_SCORE:
            self._print_menu()
            if self.decision_validator():
                self.player.player_cards.append(self.game_deck.card_taking())
                self.player.player_score_count()
                print('\nYour cards: ')
                print(f'{self.player}\n')
            else:
                break
        
        # Check the result and choos next step of the game. 
        if self.player.player_score == BLACKJACK_SCORE:
            result = '21 - BLACK JACK! You win!!'
        elif self.player.player_score < BLACKJACK_SCORE:
            self.croupier_opening()

            if self.croupier.player_score > self.player.player_score:
                result = 'Croupier wins.'
            else:
                self.croupier_turn()
                # Check the final result and determine the winner based on scores.
                if BLACKJACK_SCORE >= self.croupier.player_score > self.player.player_score:
                    result ='Croupier wins.'
                else:
                    result ='You win!!' 
        else:
            result ='Croupier wins.'

        print(result)
        return result
    def croupier_opening(self):
        """
        Initiates the croupier's turn in the Blackjack game.
        """
        for _ in range(2):
            self.croupier.player_cards.append(self.game_deck.card_taking())
        self.croupier.player_score_count()
        self._print_both_results()


    def croupier_turn(self):
        """
        Manages the croupier's turn in the Blackjack game.
        The croupier draws cards until their score is higher than the player's score or they bust.
        """
        # Croupier play loop till the score grater tahn player score. 
        while self.croupier.player_score <= self.player.player_score:

            input("Press Enter to continue... ")

            self.croupier.player_cards.append(self.game_deck.card_taking())

            self.croupier.player_score_count()
            self._print_both_results()

        
