from models import Ranking, db, Game
from schemas import ranking_schema


class RankingService:

    @classmethod
    def start_ranking_table(cls, game_id):
        ranking = Ranking(game_id=game_id)
        db.session.add(ranking)
        db.session.commit()
        return ranking_schema.dump(ranking)

    @staticmethod
    def set_winner(game_id: int, winner_id: int):
        ranking = Ranking.query.filter_by(game_id=game_id).first()
        if ranking:
            ranking.winner_id = winner_id
            db.session.add(ranking)
            db.session.commit()
