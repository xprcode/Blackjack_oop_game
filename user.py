"""
Blackjack User Module

This module reprezents 'User' class who has own score number and list of received cards 
and provides a string representation for display.
This module is used both for player and croupier in Blackjack game.

Classes:
    - User: Represents a participant in a Blackjack game.
"""

class User:
    """
    User: Represents a participant in a Blackjack game.
    """
    def __init__(self) -> None:
        self.player_score = 0
        self.player_cards = []

    def player_score_count(self):
        """
        Calculate and return the total score of the user based on their held cards.
        """
        self.player_score = 0
        ace_counter = 0

        for card in self.player_cards:
            ace_counter += 1
            # If the ace is in 2 first cards it equals 11 points.
            if len(self.player_cards) > 2 and card.value == 11 and ace_counter > 2:
                self.player_score += 1
            # If ace is not in 2 first cards it equalss 1 point.
            else:
                self.player_score += card.value
        # If user gets 2 aces as 2 first cards, score is 21 not 22.
        if len(self.player_cards) == 2 and self.player_score == 22:
            self.player_score = 21

        return self.player_score

    def __str__(self) -> str:
        """
        Generate a string representation of the user, including their cards and total score.
        """
        card_str = ''.join(f"[{card}]" for card in self.player_cards)
        return f"{card_str}\nTotal score: {self.player_score}"
    