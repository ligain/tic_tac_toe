from services.game import GameService
from tests.constants import EXPECTED_EMPTY_BOARD, EXPECTED_FULL_BOARD


def test_draw_empty_board():
    initial_board = ['_', '_', '_', '_', '_', '_', '_', '_', '_']
    result_board = GameService.draw_board(initial_board)
    assert result_board == EXPECTED_EMPTY_BOARD

def test_draw_full_board():
    initial_board = ['x', 'o', 'o', 'o', 'x', 'x', 'o', '_', 'o']
    result_board = GameService.draw_board(initial_board)
    assert result_board == EXPECTED_FULL_BOARD

def test_find_player_symbol():
    game_data = {
        "player_1_id": 1,
        "player_2_id": 2,
        "player_1_symbol": "x",
        "player_2_symbol": "o"
    }
    player_symbol = GameService.find_player_symbol(game_data=game_data, player_id=game_data.get('player_1_id'))
    assert player_symbol == game_data.get('player_1_symbol')

def test_winner_found():
    game_data = {
        "player_1_id": 1,
        "player_2_id": 2,
        "player_1_symbol": "x",
        "player_2_symbol": "o"
    }
    horizontal_win_board = ['x', 'x', 'x', 'o', '_', 'o', '_', 'x', '_']
    vertical_win_board = ['o', 'x', 'x', 'o', '_', 'o', 'o', 'x', '_']
    diagonal_win_board = ['o', 'x', '_', 'x', 'o', 'o', '_', 'x', 'o']
    game_data['board'] = horizontal_win_board
    horizontal_winner_id = GameService.define_winner(game_data=game_data)
    assert horizontal_winner_id == game_data['player_1_id']

    game_data['board'] = vertical_win_board
    horizontal_winner_id = GameService.define_winner(game_data=game_data)
    assert horizontal_winner_id == game_data['player_2_id']

    game_data['board'] = diagonal_win_board
    horizontal_winner_id = GameService.define_winner(game_data=game_data)
    assert horizontal_winner_id == game_data['player_2_id']


def test_winner_not_found():
    pass