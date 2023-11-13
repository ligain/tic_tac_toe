from itertools import repeat, compress

from constants import NULL_SYMBOL, X_SYMBOL, O_SYMBOL, BOARD_MAPPING, BOARD_TEMPLATE, WIN_COMBINATIONS
from models import db, Game
from schemas import game_schema, game_full_schema
from marshmallow import ValidationError

from services.ranking import RankingService


class GameService:
    @staticmethod
    def normalize_symbol(symbol: str) -> str:
        if isinstance(symbol, str) and symbol.lower() in (X_SYMBOL, O_SYMBOL):
            return symbol.lower()
        return NULL_SYMBOL

    @staticmethod
    def draw_board(board: list):
        """ It formats a game board looks like:
            x | o |
            ----------
            o | x | x
            ----------
            o |   | o
        """
        replaced_board = [BOARD_MAPPING[symbol] for symbol in board]
        return BOARD_TEMPLATE.format(*replaced_board)

    @classmethod
    def create_game(cls, fields: dict):
        if not fields:
            return {"message": "No input data provided"}, 400
        try:
            game_data = game_schema.load(fields, session=db.session)
        except ValidationError as err:
            return err.messages, 422
        initial_board = list(repeat(NULL_SYMBOL, 9))
        game_data.player_1_symbol = cls.normalize_symbol(game_data.player_1_symbol)
        game_data.player_2_symbol = cls.normalize_symbol(game_data.player_2_symbol)
        game_data.board = initial_board
        db.session.add(game_data)
        db.session.commit()
        RankingService.start_ranking_table(game_id=game_data.id)
        return {'game_id': game_data.id}

    @staticmethod
    def get_game_by_id(game_id: int) -> Game:
        game = db.get_or_404(Game, game_id, description='Game with specified id was not found')
        return game_full_schema.dump(game)

    @classmethod
    def get_game(cls, game_id: int):
        game_from_db = cls.get_game_by_id(game_id=game_id)
        formatted_board = cls.draw_board(board=game_from_db['board'])
        game_from_db['board'] = formatted_board
        return game_from_db

    @staticmethod
    def find_player_symbol(game_data: dict, player_id: int) -> str:
        if game_data['player_1_id'] == player_id:
            return game_data['player_1_symbol']
        if game_data['player_2_id'] == player_id:
            return game_data['player_2_symbol']

    @staticmethod
    def find_player_id_by_symbol(game_data: dict, player_symbol: str) -> int:
        if game_data['player_1_symbol'] == player_symbol:
            return game_data['player_1_id']
        if game_data['player_2_symbol'] == player_symbol:
            return game_data['player_2_id']

    @classmethod
    def define_winner(cls, game_data: dict):
        """
        Possible win combinations:
        a) horizontal
             o | o | o
            ----------
              |   |
            ----------
              |   |

        b) vervical
               | o |
            ----------
              | o |
            ----------
              | o |

        c) diagonal
             o |  |
            ----------
              | o |
            ----------
              |  | o
        """
        board = game_data.get('board', [])
        for win_combination in WIN_COMBINATIONS:
            line = set(compress(board, win_combination))
            if len(line) == 1:
                # Winner found!!!
                winner_symbol = line.pop()
                winner_id = cls.find_player_id_by_symbol(game_data=game_data, player_symbol=winner_symbol)
                return winner_id

        # Continue game. Winner not defined.

    @staticmethod
    def change_board(board: list, position: int, symbol: str) -> list[str]:
        """Makes a turn on the board"""
        board[position] = symbol
        return board

    @classmethod
    def make_turn(cls, game_id: int, player_id: int, position: int):
        winner_response = {}
        game_data = cls.get_game_by_id(game_id=game_id)
        player_symbol = cls.find_player_symbol(game_data=game_data, player_id=player_id)
        updated_board = cls.change_board(board=game_data['board'], position=position, symbol=player_symbol)
        game_data['board'] = updated_board
        winner_id = cls.define_winner(game_data=game_data)
        if winner_id:
            RankingService.set_winner(game_id=game_id, winer_id=winner_id)
            winner_response = {'winner_id': winner_id}
        game_obj = game_full_schema.load(game_data, session=db.session)
        db.session.add(game_obj)
        db.session.commit()
        return winner_response or game_data
