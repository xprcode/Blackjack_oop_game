"""
Blackjack Deck Module

This module reprezents the 'Deck' class.  
It initialize the deck of 52 game cards , shuffel it and giving the card from the top
of the deck to the player or croupier. 

Classes:
    - Deck: Manages the creation, shuffling, and distribution of a deck of cards.

External Dependencies:
    - 'Card' class from the 'card' module.
"""

from random import shuffle
from card import Card

class Deck:
    """
    Reprezent, initialize, shuffle and giving cards from the deck to users. 
    """
    def __init__(self) -> None:
        self.card_list = []
        Deck.initialize_deck(self)

    def initialize_deck(self):
        """
        Initialize the deck of 52 cards in 4 colours, 14 value represented by numbers.
        Returns:
            List: list of 52 Card objects. 
        """
        deck = list(range(1, 14))
        for card in deck:
            for colour in Card.colours:
                self.card_list.append(
                    Card(
                        value = card,
                        number_repr = card,
                        colour = colour,
                    )
                    )

        return self.card_list

    def shuffle(self):
        """
        Shuffle the list of the card each time in random order. 
        """
        shuffle(self.card_list)

    def card_taking(self):
        """
        Give one card from the top of the deck to the user and remove the card from the deck. 

        Returns:
            Card subject: card object from the end of cardlist. 
        """
        return self.card_list.pop()
    