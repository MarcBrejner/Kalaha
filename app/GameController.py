import numpy as np

class GameController:
    def __init__(self, model):
        self.model = model

    def isGameOver(self):
        if (self.model.gameState[0][:-1].sum() + self.model.gameState[0][:-1].sum()) > 0:
            return False
        if self.model.gameState[0][-1] > self.model.gameState[1][-1]:
            print("Player one won")
        else:
            print("Player two won")
        return True

    def turn(self, cup, player):
        if cup < 0 or cup > (self.model.gameState[player].size - 2):
            return

        shells = self.model.gameState[player][cup]
        self.model.gameState[player][cup] = 0

        while shells > 0:
            cup += 1

            self.model.gameState[player][cup] += 1

            if cup >= (self.model.gameState[player].size-1):
                # swap player array
                player = 1 - player
                cup = 0

            shells -= 1
        self.isGameOver()









