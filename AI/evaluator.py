from game_enum import GameEnum

class GameController:
    def __init__(self, model):
        self.gameState = model.gameState

    def conclude(self, turn):
        #if all cups on side is empty, opponent captures all their remaining shells, and game ends
        if self.gameState[0][:-1].sum() == 0:
            self.gameState[1][-1] += self.gameState[1][:-1].sum()
            self.gameState[1][:-1].fill(0)
            return self.check_win()
        elif self.gameState[1][:-1].sum() == 0:
            self.gameState[0][-1] += self.gameState[0][:-1].sum()
            self.gameState[0][:-1].fill(0)
            return self.check_win()
        #else, if game has not ended, gives current player an extra turn in case he ended his turn in his own store
        elif turn:
            return GameEnum.extra_turn
        else:
            return GameEnum.standard

    def check_win(self):
        if self.gameState[0][-1] > self.gameState[1][-1]:
            return GameEnum.player_one_win
        else:
            return GameEnum.player_two_win

    def steal_shells(self, player, position):
        #find opposite cup, and steal shells
        stolen_shells = self.gameState[1-player][abs(position-(self.gameState[player].size-2))]
        self.gameState[1 - player][abs(position - (self.gameState[player].size-2))] = 0

        #also capture the shell from own cup
        self.gameState[player][position] = 0
        stolen_shells += 1

        #add shells to own stores
        self.gameState[player][-1] += stolen_shells


    def turn(self, cup, player):
        extra_turn = False
        position = cup
        original_player = player

        #take all shells from chosen cup
        shells = self.gameState[player][cup]
        self.gameState[player][cup] = 0

        #Keep distributing shells as long as they are in stock
        while shells > 0:
            #Increment position
            position += 1
            #Check if new position is one of the stores
            if position >= (self.gameState[player].size-1):
                if player == original_player:
                    self.gameState[player][position] += 1
                    #jump to opposite side position is store
                    player = 1 - player
                    position = -1
                else:
                    #In case the new position is opponent score, skip it and increment the first cup on own half instead.
                    player = 1 - player
                    position = 0
                    self.gameState[player][position] += 1
            else:
                self.gameState[player][position] += 1
            shells -= 1

        #If turn ended in store, grant extra turn, else check if end cup was empty, in which case steal shells from opposite cup.
        if position == -1:
            extra_turn = True
        elif player == original_player and self.gameState[player][position] == 1:
            self.steal_shells(player, position)

        return self.conclude(extra_turn)