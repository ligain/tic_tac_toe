from flask import request
from flask_restful import Resource
from services.player import PlayerService


class Player(Resource):
    def get(self, player_id):
        """Get details for a single player"""
        player = PlayerService.get_player_by_id(player_id=player_id)
        return player

    def delete(self, player_id):
        """Delete a single player"""
        deleted_player_id = PlayerService.delete_player_by_id(player_id=player_id)
        return deleted_player_id

class PlayersListCreate(Resource):
    def get(self):
        """List players table"""
        all_players = PlayerService.get_all_players()
        return all_players

    def post(self):
        """Create a single player"""
        created_player = PlayerService.create_player(fields=request.get_json())
        return created_player