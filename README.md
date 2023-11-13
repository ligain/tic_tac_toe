# Tic-Tac-Toe game

Flask API for Tic-Tac-Toe game.

| x | o | x |
|--|--|--|
| x | o | |
|  | o |  |

Game rules you can read on the [Wiki](https://en.wikipedia.org/wiki/Tic-tac-toe).

# Installation

1. Install [Docker](https://www.docker.com/) & [docker-compose](https://docs.docker.com/compose/).
2. Run command ```$ docker-compose up```
3. You should see app up and running:
```app-flask |  * Serving Flask app 'factory'
app-flask |  * Debug mode: on
app-flask | WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
app-flask |  * Running on all addresses (0.0.0.0)
app-flask |  * Running on http://127.0.0.1:5000
app-flask |  * Running on http://172.30.0.3:5000
app-flask | Press CTRL+C to quit
app-flask |  * Restarting with stat
app-flask |  * Debugger is active!
app-flask |  * Debugger PIN: 864-898-749
```
4. Open http://127.0.0.1:5000
5. To shut down project run command ```$ docker-compose down```

# Api reference
## Player API
| Operation              | cURL request                                    | Sample response                                                            |
|------------------------|-------------------------------------------------|----------------------------------------------------------------------------|
| Get all players        | curl --location 'http://127.0.0.1:5000/player/' |                                                                            |
| Create a player        | curl --location 'http://127.0.0.1:5000/player/' --header 'Content-Type: application/json' --data-raw '{    "username": "Andrey",    "email": "andrey@example.com",    "age": 30}' | {"id": 2, "username": "Andrey", "email": "andrey@example.com", "age": 30 } |
| Get a single player    | curl --location 'http://127.0.0.1:5000/player/2' | {"id": 2, "username": "Andrey", "email": "andrey@example.com", "age": 30 } |
| Delete a single player | curl --location --request DELETE 'http://127.0.0.1:5000/player/1' | 1 |

## Game API
Operation: **Create a new game**

cURL request: 
``` 
curl --location 'http://127.0.0.1:5000/game/' --header 'Content-Type: application/json' --data '{
    "player_1_id": 1,
    "player_2_id": 2,
    "player_1_symbol": "x",
    "player_2_symbol": "O"
}
```

Sample response: 
```
{
    "game_id": 2
}
```


Operation: **Get the game details**

cURL request: 
``` 
curl --location 'http://127.0.0.1:5000/game/1'
```

Sample response: 
```
{
    "id": 1,
    "player_1_id": 1,
    "player_2_id": 2,
    "board": "\n  |   |  \n----------\n  |   |  \n----------\n  |   |  ",
    "player_1_symbol": "x",
    "player_2_symbol": "o"
}
```

Operation: **Make a turn**

cURL request: 
``` 
curl --location --request PUT 'http://127.0.0.1:5000/game/1' --header 'Content-Type: application/json' --data '{
    "player_id": 1,
    "position": 2
}'
```

Sample response if someone wins: 
```
{
    "winner_id": 1
}
```

## Ranking API
Operation: **Create league (ranking) table**

cURL request: 
``` 
curl --location 'http://127.0.0.1:5000/ranking/' --header 'Content-Type: application/json' --data '{
    "game_id": 2
}'
```

Sample response if someone wins: 
```
{
    "id": 3
}
```

