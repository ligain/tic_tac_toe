from flask_migrate import Migrate
import sqlalchemy as sa
from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column, DeclarativeBase
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import scoped_session, sessionmaker


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

