# Tic-Tac-Toe game

Simple Flask API for Tic-Tac-Toe game.

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

# Api reference
| Operation              | cURL request                                    | Sample response                                                            |
|------------------------|-------------------------------------------------|----------------------------------------------------------------------------|
| Get all players        | curl --location 'http://127.0.0.1:5000/player/' |                                                                            |
| Create a player        | curl --location 'http://127.0.0.1:5000/player/' --header 'Content-Type: application/json' --data-raw '{    "username": "Andrey",    "email": "andrey@example.com",    "age": 30}' | {"id": 2, "username": "Andrey", "email": "andrey@example.com", "age": 30 } |
| Get a single player    | curl --location 'http://127.0.0.1:5000/player/2' | {"id": 2, "username": "Andrey", "email": "andrey@example.com", "age": 30 } |
| Delete a single player | curl --location --request DELETE 'http://127.0.0.1:5000/player/1' | 1 |



