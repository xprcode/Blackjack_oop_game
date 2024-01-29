from game import Game
from user import User


def test_start_to_play():
    game = Game()
    player = User()
    game.player = player
    game.start_to_play()

    assert len(player.player_cards) == 2
    assert player.player_score != 0

def test_mid_end_game_blackjack():
    game = Game()
    player = User()
    game.player = player
    player.player_score = 21
    result = game.mid_end_game()
    assert result == '21 - BLACK JACK! You win!!'

def test_mid_end_game_croupier_wins():
    game = Game()
    player = User()
    croupier = User()

    game.player = player
    game.croupier = croupier

    player.player_score = 22
    croupier.player_score = 20
    result = game.mid_end_game()
    
    assert result == 'Croupier wins.'

