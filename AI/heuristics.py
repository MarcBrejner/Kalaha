def count_player_shells(board, player):
    player_shells = 0
    player_shells += board[player][:-1].sum()
    player_shells += board[player][-1] * 1.5
    return player_shells


def heuristics(board):
    player_one_shells = count_player_shells(board, 0)
    player_two_shells = count_player_shells(board, 1)

    return player_one_shells - player_two_shells
