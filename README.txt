Kalaha game and AI for the first assignment in Introduction to Artificial Intelligence course at DTU 02180 March 2022

The game uses a client-server structure, the server is the board, and controls all game logic, and the clients are the players.
A client can either be a real player, or an AI, but from the servers perspective they are the same.

A client can be either: ai_r.py which runs an AI taking random moves, ai.py which is an AI using the min-max algorithm with alpha-beta pruning and the heuristic discussed in the report,
or client.py which is for takes human player inputs.

The project uses the python package numpy which might need to be installed, if not already installed.

To run the game:
1. Open three terminals.
2. Open the server in one terminal, using "py server.py"
3. In the other two terminals, open two of the available clients (client.py, ai.py or ai_r.py)

in ai.py, the variable which_fct can be changed to select one of the other heuristics,
and search_depth can be changed to change the depth.