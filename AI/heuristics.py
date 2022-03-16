def count_player_shells(game_state, player):
    player_shells = 0
    player_shells += game_state[player][:-1].sum()
    player_shells += game_state[player][-1] * 1.5
    return player_shells


def heuristics(game_state):
    player_one_shells = count_player_shells(game_state, 0)
    player_two_shells = count_player_shells(game_state, 1)

    return player_one_shells - player_two_shells
