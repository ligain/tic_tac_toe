from flask_restful import Api
from flask_marshmallow import Marshmallow
from factory import create_app
from resources.player import Player, PlayersListCreate

app = create_app()
api = Api(app)
ma = Marshmallow(app)

api.add_resource(PlayersListCreate, '/player/')
api.add_resource(Player, '/player/<int:player_id>')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')