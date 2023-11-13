from sqlalchemy import Integer, String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, DeclarativeBase
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.dialects.postgresql import ARRAY
from sqlalchemy_utils import ScalarListType, ChoiceType

from constants import X_SYMBOL, O_SYMBOL


class Base(DeclarativeBase):
  pass

db = SQLAlchemy(model_class=Base)


class Player(db.Model):
    __tablename__ = 'players'

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    username: Mapped[str] = mapped_column(String, unique=True, nullable=False)
    email: Mapped[str] = mapped_column(String)
    age: Mapped[str] = mapped_column(Integer)

    def __repr__(self):
        return f'Player <{self.id}>'


class Game(db.Model):
    SYMBOL_CHOICES = [
        (X_SYMBOL, X_SYMBOL),
        (O_SYMBOL, O_SYMBOL)
    ]

    __tablename__ = 'games'
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    player_1_id: Mapped[int] = mapped_column(Integer, ForeignKey("players.id"))
    player_2_id: Mapped[int] = mapped_column(Integer, ForeignKey("players.id"))
    board: Mapped[list[str]] = mapped_column(ARRAY(String(9)))
    player_1_symbol: Mapped[str] = mapped_column(ChoiceType(SYMBOL_CHOICES))
    player_2_symbol: Mapped[str] = mapped_column(ChoiceType(SYMBOL_CHOICES))

    def __repr__(self):
        return f'Game <Player 1: {self.player_1_id}, Player 2: {self.player_2_id}>'


class Ranking(db.Model):
    __tablename__ = 'rankings'
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    game_id: Mapped[int] = mapped_column(Integer, ForeignKey("games.id"))
    winner_id: Mapped[int] = mapped_column(Integer, ForeignKey("players.id"), nullable=True)

    def __repr__(self):
        return f'Ranking <Game id: {self.game_id}'
