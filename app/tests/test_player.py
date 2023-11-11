import os

import pytest
from sqlalchemy_utils import database_exists, create_database, drop_database
from werkzeug.exceptions import NotFound

from factory import create_app
from services.player import PlayerService
from tests.constants import PLAYER_PAYLOAD_1, PLAYER_PAYLOAD_2, PLAYER_PAYLOAD_3


@pytest.fixture(scope="session")
def app():
    config = os.getenv('TEST_APP_SETTINGS')
    test_db_url = os.getenv('TEST_DATABASE_URL')
    if not database_exists(test_db_url):
        create_database(test_db_url)

    app = create_app(config=config)
    yield app
    if database_exists(test_db_url):
        drop_database(test_db_url)


@pytest.fixture
def app_ctx(app):
    with app.app_context():
        yield


@pytest.fixture(scope="session")
def db(app):
    yield app.extensions.get('sqlalchemy')


@pytest.mark.usefixtures("app_ctx")
def test_create_player(app):
    created_player = PlayerService.create_player(fields=PLAYER_PAYLOAD_1)
    created_player_from_db = PlayerService.get_player_by_id(player_id=created_player.get('id'))
    assert created_player
    assert created_player.get('username') == PLAYER_PAYLOAD_1.get('username')
    assert created_player_from_db.get('id') == created_player.get('id')
    PlayerService.delete_player_by_id(player_id=created_player_from_db.get('id'))

@pytest.mark.usefixtures("app_ctx")
def test_delete_player(app):
    created_player = PlayerService.create_player(fields=PLAYER_PAYLOAD_1)
    assert created_player
    deleted_player_id = PlayerService.delete_player_by_id(player_id=created_player.get('id'))
    assert deleted_player_id
    with pytest.raises(NotFound):
        PlayerService.get_player_by_id(player_id=deleted_player_id)


@pytest.mark.usefixtures("app_ctx")
def test_create_multiple_players(app):
    created_player_1 = PlayerService.create_player(fields=PLAYER_PAYLOAD_3)
    created_player_2 = PlayerService.create_player(fields=PLAYER_PAYLOAD_2)
    players_count = len([created_player_1, created_player_2])
    created_players_from_db = PlayerService.get_all_players()
    assert players_count == len(created_players_from_db)
