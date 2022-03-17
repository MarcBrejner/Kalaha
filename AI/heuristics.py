def count_player_shells(game_state, player):
    player_shells = 0
    for i in range(6):
        player_shells += game_state[player][i].sum()
    player_shells += game_state[player][6] * 1.5
    return player_shells


def heuristics(game_state):
    player_one_shells = count_player_shells(game_state, 0)
    player_two_shells = count_player_shells(game_state, 1)

    return player_one_shells - player_two_shells
