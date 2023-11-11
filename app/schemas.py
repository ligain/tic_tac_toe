from marshmallow_sqlalchemy import SQLAlchemyAutoSchema

from models import Player


class PlayerSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Player
        load_instance = True


player_schema = PlayerSchema()
