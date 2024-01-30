from card import Card

 
def test_representatnion():
    """ Check if proper card represtatnion is printed."""
    card = Card(1, '♠', 1)
    assert str(card) == 'A of ♠'

 
def test_card_creation():
    """ Check if create card with proper value and colour."""
    card = Card(2, '♥', 2)
    assert card.value == 2
    assert card.colour == '♥'



