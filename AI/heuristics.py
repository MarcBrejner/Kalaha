def count_player_shells(game_state, player, which_fct):
    player_shells = 0
    if which_fct == 0:
        player_shells = game_state[player][6]

    if which_fct == 1:
        for i in range(6):
            player_shells += game_state[player][i].sum()

    if which_fct == 2:
        for i in range(6):
            player_shells += game_state[player][i].sum()
        player_shells += game_state[player][6] * 1.5

    if which_fct == 3:
        for i in range(6):
            if game_state[player][i] == (6 - i):
                player_shells += 2
            if game_state[player][i] == 0:
                player_shells += 1
            if game_state[player][i] == 13:
                player_shells += 4
        player_shells += game_state[player][6] * 4

    return player_shells


def heuristics(game_state, which_fct):
    player_one_shells = count_player_shells(game_state, 0, which_fct)
    player_two_shells = count_player_shells(game_state, 1, which_fct)
    return player_one_shells - player_two_shells