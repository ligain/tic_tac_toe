from marshmallow_sqlalchemy import SQLAlchemyAutoSchema, SQLAlchemySchema, auto_field

from models import Player, Game, Ranking


class PlayerSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Player
        load_instance = True


class GameSchema(SQLAlchemySchema):
    class Meta:
        model = Game
        include_relationships = True
        load_instance = True

    player_1_id = auto_field()
    player_2_id = auto_field()
    player_1_symbol = auto_field()
    player_2_symbol = auto_field()


class GameFullSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Game
        include_relationships = True
        load_instance = True
        include_fk = True


class RankingSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Ranking
        load_instance = True


player_schema = PlayerSchema()
game_schema = GameSchema()
game_full_schema = GameFullSchema()
ranking_schema = RankingSchema()
