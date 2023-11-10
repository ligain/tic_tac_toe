from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column, DeclarativeBase
from flask_sqlalchemy import SQLAlchemy


class Base(DeclarativeBase):
  pass

db = SQLAlchemy(model_class=Base)


class Player(db.Model):
    __tablename__ = 'players'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    username: Mapped[str] = mapped_column(String, unique=True, nullable=False)
    email: Mapped[str] = mapped_column(String)

    def __repr__(self):
        return f'Player <{self.id}>'

