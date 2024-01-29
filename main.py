"""
Blackjack Game Module
This module contains the implementation of a simple Blackjack game.
The game involves a player competing against a computer-controlled croupier
to achieve a score as close to 21 as possible without exceeding it.

Classes:
- Game: Represents the main game logic and flow.
- Deck: Represents a deck of playing cards and provides methods for shuffling and card drawing.
- Participant: Represents a player or the croupier, keeping track of their cards and score.
"""

from game import Game


def main():
    """
    The main function to start the Blackjack game.

    This function creates an instance of the Blackjack game (Game class) 
    and initiates the player's opening move.
    It is the entry point for the execution of the Blackjack game.

    """

    game = Game()
    game.start_to_play()
    game.mid_end_game()

if __name__ == "__main__":
    main()
