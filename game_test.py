from game import Game
from user import User


def test_start_to_play():
    """ Check if player get 2 cards and any score."""
    game = Game()
    player = User()

    game.player = player
    game.start_to_play()

    assert len(player.player_cards) == 2
    assert player.player_score != 0


def test_mid_end_game_blackjack():
    """ Check the game result when player get 21 points."""
    game = Game()
    player = User()
    game.player = player
    player.player_score = 21
    result = game.mid_end_game()

    assert result == '21 - BLACK JACK! You win!!'


def test_mid_end_game_croupier_wins():
    """ Check the game result when player get more then 21 points."""
    game = Game()
    player = User()
    croupier = User()

    game.player = player
    game.croupier = croupier

    player.player_score = 22
    croupier.player_score = 20
    result = game.mid_end_game()

    assert result == 'Croupier wins.'


def test_croupier_opening():
    """Check if player get 2 cards and any score. """
    game = Game()
    croupier = User()

    game.player = croupier
    game.start_to_play()

    assert len(croupier.player_cards) == 2
    assert croupier.player_score != 0
