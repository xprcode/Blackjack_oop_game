from card import Card
from user import User

def test_calculate_player_points_3rd_card_ace():
    """[3 of ♠] + [2 of ♥] + [A of ♥]"""
    card1 = Card(3, '♠', 3) #[3]
    card2 = Card(2, '♥', 2) #[2]
    card3 = Card(1, '♥', 1) #[A]

    player = User()
    player.player_cards.append(card1)
    player.player_cards.append(card2)
    player.player_cards.append(card3)

    assert player.player_score_count() == 6

def test_calculate_player_points_2_aces():
    """[A of ♠] + [A of ♥]"""

    card1 = Card(1, '♠', 1) #[A]
    card2 = Card(1, '♥', 1) #[A]

    player = User()
    player.player_cards.append(card1)
    player.player_cards.append(card2)

    assert player.player_score_count() == 21

def test_calculate_player_points_1_ace():
    """[A of ♠] + [K of ♥]"""

    card1 = Card(1, '♠', 1) #[A]
    card2 = Card(13, '♥', 13) #[K]

    player = User()
    player.player_cards.append(card1)
    player.player_cards.append(card2)

    assert player.player_score_count() == 21

def test_calculate_player_points_no_ace():
    """[8 of ♠] + [K of ♥]"""

    card1 = Card(8, '♠', 8) #[8]
    card2 = Card(13, '♥', 13) #[K]

    player = User()
    player.player_cards.append(card1)
    player.player_cards.append(card2)

    assert player.player_score_count() == 18
