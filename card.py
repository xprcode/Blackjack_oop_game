"""
Blackjack Card Module

This module defines the 'Card' class, representing a playing card in the game of Blackjack.
Each card has a value, a string representation for numbers, and a color.

Classes:
    - Card: Represents a playing card.
"""

class Card:
    """
    Initialize a Card object with a given value, color, and number representation.
    """
    colours = ['♠','♥','♣','♦']

    def __init__(self, value, colour, number_repr) -> None:
        """
        Initialize a Card object.
        Args:
            value (int): The numeric value of the card.
            colour (str): The color (suit) of the card.
            number_repr (int): The numeric representation of the card.
        """

        self.value = self._special_cards(value)
        self.number_repr = self._number_repr(number_repr)
        self.colour = colour


    @staticmethod
    def _special_cards(number):
        """
        Static method that handles special card values (11, 12, 13).
        Args:
            number (int): The numeric value of the card.
        Returns:
            int: The adjusted numeric value for special cards.
        """
        if number in (11, 12, 13):
            number = 10
        if number == 1:
            number = 11
        return number

    @staticmethod
    def _number_repr(number_repr):
        if number_repr == 1:
            number_repr = 'A'
        elif number_repr == 11:
            number_repr = 'J'
        elif number_repr == 12:
            number_repr = 'Q'
        elif number_repr == 13:
            number_repr = 'K'
        return number_repr


    def __repr__(self) -> str:
        """
        Returns a string representation of the card.
        Returns:
            str: A string representation of the card.
        """
        return f'{self.number_repr} of {self.colour}'
