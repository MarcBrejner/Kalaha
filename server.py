import socket
import pickle
from _thread import *

from app.game_controller import GameController
from app.game_model import GameModel
from game_enum import GameEnum

host = "127.0.0.1"
port = 13000
your_turn = str.encode("Your turn")
get_game_state = "getGameState"
you_won = str.encode("You won!")
player_number = 1
sleep_time = 0.5

player_won = {
    1: str.encode("Player one won!"),
    2: str.encode("Player two won!")
}

player_connection = {
    1: None,
    2: None
}

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try: 
    socket.bind((host, port))
except socket as e:
    print(e)

socket.listen(2)

gameController = GameController(GameModel())
print("Server has been started, waiting for players")


def end_game():
    player_connection[1].close()
    player_connection[2].close()


def send_player_win(winning_player, losing_player):
    send_game_state(winning_player)
    send_to_player(you_won, winning_player)
    send_to_player(player_won[winning_player], losing_player)
    end_game()


def send_game_state(current_player):
    game_model = gameController.gameState
    data_string = pickle.dumps(game_model)
    print(f"Sending game_state to player: {current_player}")
    send_to_player(data_string, current_player)


def send_to_player(encoded_data, player):
    player_connection[player].sendall(encoded_data)


def send_player_number(player):
    print(f"Sending player_number to player: {player}")
    send_to_player(str.encode(str(player)), player)


def start_when_player_two_joins(player):
    if player == 2:
        send_your_turn(1)


def send_your_turn(player):
    print(f"Sending your_turn to player: {player}")
    send_to_player(your_turn, player)


def check_command(command, current_player):
    if command == get_game_state:
        send_game_state(current_player)

    elif command.isdigit():
        turn_result = gameController.turn(int(command)-1, current_player-1)
        print(turn_result)
        if turn_result == GameEnum.standard:
            if current_player == 1:
                send_your_turn(2)
            else:
                send_your_turn(1)

        elif turn_result == GameEnum.extra_turn:
            player_connection[current_player].recv(2048).decode()
            send_game_state(current_player)
            print(f"Sending your_turn to player: {current_player}")
            send_to_player(your_turn, current_player)

        elif turn_result == GameEnum.player_one_win:
            send_player_win(current_player, 2)

        elif turn_result == GameEnum.player_two_win:
            send_player_win(current_player, 1)

        else:
            print("Unknown turn result")


def threaded_client(client_connection, player):
    send_player_number(player)
    start_when_player_two_joins(player)
    while True:
        try:
            command = client_connection.recv(2048).decode()
            print(f"Received command {command} from player {player}")

            if not command:
                print("Disconnected")
                break
            else:
                check_command(command, player)

        except:
            break

    print("Lost connection")
    client_connection.close()


while True:
    connection, addr = socket.accept()

    if player_number < 3:
        print("Connected to: ", addr)
        start_new_thread(threaded_client, (connection, player_number))
        player_connection[player_number] = connection

        player_number += 1
    else:
        print("Two players already connected")
        connection.close()



