from card import Card

# Check if proper card represtatnion is printed. 
def test_representatnion():
    card = Card(1, '♠', 1)
    assert str(card) == 'A of ♠'

#Check if create card with proper value and colour. 
def test_card_creation():
    card = Card(2, '♥', 2)
    assert card.value == 2
    assert card.colour == '♥'



