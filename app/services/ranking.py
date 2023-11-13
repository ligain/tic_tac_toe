from models import Ranking, db, Game


class RankingService:

    @classmethod
    def start_ranking_table(cls, game_id):
        ranking = Ranking(game_id=game_id)
        db.session.add(ranking)
        db.session.commit()
        return ranking

    @staticmethod
    def set_winner(game_id: int, winer_id: int):
        ranking = Ranking.query.filter_by(game_id=game_id).first()
        if ranking:
            ranking.winner_id = winer_id
            db.session.add(ranking)
            db.session.commit()
