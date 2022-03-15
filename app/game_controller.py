import enum

class GameEnum(enum.Enum):
    standard = 1
    extra_turn = 2
    player_one_win = 3
    player_two_win = 4

class GameController:
    def __init__(self, model):
        self.model = model

    def conclude(self, turn):
        if (self.model.gameState[0][:-1].sum() + self.model.gameState[0][:-1].sum()) > 0:
            if self.model.gameState[0][-1] > self.model.gameState[1][-1]:
                return GameEnum.player_one_win
            else:
                return GameEnum.player_two_win
        if turn:
            return GameEnum.extra_turn
        return GameEnum.standard


    def turn(self, cup, player):
        extra_turn = False
        original_cup = cup
        original_player = player
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
                cup = -1

            shells -= 1
        if int(original_cup) == 4:
            extra_turn = True

        return self.conclude(extra_turn)









