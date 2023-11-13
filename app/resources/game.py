from flask import request
from flask_restful import Resource

from services.game import GameService


class StartGame(Resource):
    def post(self):
        """Start a game"""
        created_game = GameService.create_game(fields=request.get_json())
        return created_game


class UpdateDetailsGame(Resource):
    def put(self, game_id: int):
        """Make a turn"""
        request_body = request.get_json()
        game_result = GameService.make_turn(
            game_id=game_id,
            player_id=request_body.get('player_id'),
            position=request_body.get('position')
        )
        return game_result

    def get(self, game_id: int):
        """Get game info and view a board"""
        game = GameService.get_game(game_id=game_id)
        return game