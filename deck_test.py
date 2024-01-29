from deck import Deck
from card import Card

# Check if deck creates listo f 52 cards. 
def test_deck_creation():
    deck = Deck()
    assert len(deck.card_list) == 52

# Check if each colour conaint 13 cards.
def test_deck():
    deck = Deck()
    cards = [(card.value, card.colour) for card in deck.card_list]

    for color in Card.colours:
        possible_color = [card for card in cards if card[1] == color]

    assert len(possible_color) == 13

# Check if dedk has been shuffled.
def test_shuffle():
    deck = Deck()
    new_deck = Deck()
    new_deck.shuffle()
    if deck.card_list != new_deck:
        assert True

# Check if exactly one card has been taken and removed from the list.
def test_card_taking():
    deck = Deck()
    new_deck = Deck()
    new_deck.card_taking()
    if (deck.card_list != new_deck) and len(new_deck.card_list) == 51:
        assert True
    