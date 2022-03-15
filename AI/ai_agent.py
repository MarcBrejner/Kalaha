from network import Network
import pickle

network = Network()
game_running = True


player = network.get_player_number()
while game_running:
    print(network.wait_for_turn())

    game_state = pickle.loads(network.get_game_state())

    player_move = input("Enter next move: ")
    response = network.take_turn(player_move)

    game_state = pickle.loads(network.get_game_state())
