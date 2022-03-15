import enum

class GameEnum(enum.Enum):
    standard = 1
    extra_turn = 2
    player_one_win = 3
    player_two_win = 4

class GameController:
    def __init__(self, model):
        self.gameState = model.gameState

    def conclude(self, turn):
        if (self.gameState[0][:-1].sum() + self.gameState[0][:-1].sum()) > 0:
            if self.gameState[0][-1] > self.gameState[1][-1]:
                return GameEnum.player_one_win
            else:
                return GameEnum.player_two_win
        if turn:
            return GameEnum.extra_turn
        return GameEnum.standard


    def turn(self, cup, player):
        extra_turn = False
        position = cup
        original_cup = self.gameState[player][cup]
        original_player = player
        if cup < 0 or cup > (self.gameState[player].size - 2):
            return

        shells = self.gameState[player][cup]
        self.gameState[player][cup] = 0

        while shells > 0:
            position += 1
            if position >= (self.gameState[player].size-1):
                if self.gameState[player][position] != self.gameState[1-original_player][self.gameState[player].size-1]:
                    self.gameState[player][position] += 1
                    # swap player array
                    player = 1 - player
                    position = -1
                else:
                    self.gameState[player][position] += 1
                    player = 1 - player
                    position = -1
            else:
                self.gameState[player][position] += 1
            shells -= 1
        if int(original_cup) == 4:
            extra_turn = True

        return self.conclude(extra_turn)









