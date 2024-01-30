from deck import Deck
from card import Card

 
def test_deck_creation():
    """ Check if deck creates listo f 52 cards."""
    deck = Deck()
    assert len(deck.card_list) == 52


def test_deck():
    """ Check if each colour conaint 13 cards."""
    deck = Deck()
    cards = [(card.value, card.colour) for card in deck.card_list]

    for color in Card.colours:
        possible_color = [card for card in cards if card[1] == color]

    assert len(possible_color) == 13


def test_shuffle():
    """ Check if dedk has been shuffled."""
    deck = Deck()
    new_deck = Deck()
    new_deck.shuffle()
    if deck.card_list != new_deck:
        assert True


def test_card_taking():
    """ Check if exactly one card has been taken and removed from the list."""
    deck = Deck()
    new_deck = Deck()
    new_deck.card_taking()
    if (deck.card_list != new_deck) and len(new_deck.card_list) == 51:
        assert True
    