from typing import Union

from models import db, Player
from schemas import player_schema
from marshmallow import ValidationError


class PlayerService:
    @staticmethod
    def create_player(fields: dict) -> Union[dict, tuple]:
        if not fields:
            return {"message": "No input data provided"}, 400
        try:
            player_data = player_schema.load(fields, session=db.session)
        except ValidationError as err:
            return err.messages, 422
        db.session.add(player_data)
        db.session.commit()
        return player_schema.dump(player_data)

    @staticmethod
    def get_player_by_id(player_id: int) -> dict:
        player = db.get_or_404(Player, player_id, description='Object with specified id was not found')
        return player_schema.dump(player)

    @classmethod
    def delete_player_by_id(cls, player_id: int) -> int:
        player = db.get_or_404(Player, player_id, description='Object with specified id was not found')
        db.session.delete(player)
        db.session.commit()
        return player_id

    @staticmethod
    def get_all_players() -> dict:
        quotes = Player.query.all()
        result = player_schema.dump(quotes, many=True)
        return result