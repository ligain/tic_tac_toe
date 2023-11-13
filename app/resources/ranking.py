from flask import request
from flask_restful import Resource

from services.ranking import RankingService


class RankingCreate(Resource):
    def post(self):
        """Creates a league season table"""
        request_data = request.get_json()
        ranking = RankingService.start_ranking_table(game_id=request_data.get('game_id'))
        return ranking