import numpy as np


class GameModel:
    def __init__(self):
        self.gameState = np.array([4, 4, 4, 4, 4, 4, 0], [4, 4, 4, 4, 4, 4, 0])
        self.currentPlayerTurn = 0

    def get_game_state(self):
        return self.gameState

    def set_game_state(self, updated_game_state: np.array):
        self.gameState = updated_game_state

    def get_current_player_turn(self):
        return self.currentPlayerTurn

    def switch_current_player_turn(self):
        if self.currentPlayerTurn == 1:
            self.currentPlayerTurn = 0
        else:
            self.currentPlayerTurn = 1
