
'''
Save a copy of current game board and get score for it
'''
import json

class State:
    # game is a copy of the entire board
    # current_board tracks which board we are in
    # choice is the move we choose
    def __init__(self, game, current_board, choice, player):
        self.game = game
        self.board = current_board
        self.choice = choice
        self.player = player

    def human(self):
        print('B{}C{}P{}'.format(self.board, self.choice, self.player))

    def get_score(self):
        return self._heuristic()

    def _copy(self, game):
        new_game = [[0] * 10]
        for num in range(1, 10):
            new_game.append(game[num].copy())
        return new_game

    def new_state(self, new_choice, player):
        if self.game[self.choice][new_choice] > 0:
            # illegal
            return None
        # copy current board and place new choice
        new_game = self._copy(self.game)
        new_game[self.choice][new_choice] = player
        return State(new_game, self.choice, new_choice, player)

    # get current state
    # 0 -> no wins
    # 1 -> AI wins
    # 2 -> opponent wins
    def current_state(self):
        win = 0
        curr_game = self.game[self.board]

        # check rows
        for i in range(1, 4):
            start = i * 3 - 2
            if curr_game[start] > 0 and curr_game[start] == curr_game[start + 1] == curr_game[start + 2]:
                return curr_game[start]

        # check columns
        for i in range(1, 4):
            if curr_game[i] > 0 and curr_game[i] == curr_game[i + 3] == curr_game[i + 6]:
                return curr_game[i]
        
        # check diagonals
        if curr_game[1] > 0 and curr_game[1] == curr_game[5] == curr_game[9]:
            return curr_game[1]
        if curr_game[3] > 0 and curr_game[3] == curr_game[5] == curr_game[7]:
            return curr_game[3]

        # no wins
        return win

    def _positive(self, num):
        if num == 0:
            return 0
        return 1 if num == 1 else -1
    
    def _same(self, board, list):
        temp = board[list[0]]
        for i in range(1, len(list)):
            if not temp == board[list[i]]:
                return False
        return True

    def _empty(self, board, choice):
        return board[choice] == 0

    def _heuristic(self):
        score = 0
        all_wins = [[1, 2, 3], [4, 5, 6], [7, 8, 9],
            [1, 4, 7], [2, 5, 8], [3, 6, 9],
            [1, 5, 9], [3, 5, 7]]
        weight = [[0, -10, -100, -1000],
            [10, 0, 0, 0],
            [100, 0, 0, 0],
            [1000, 0, 0, 0]]

        for num in range(1, 10):
            curr_board = self.game[num]
            for i in range(0, 8):
                temp = player = opponent = 0
                for j in range(0, 3):
                    curr = curr_board[all_wins[i][j]]
                    if curr == 1:
                        player += 1
                    elif curr == 2:
                        opponent += 1
                temp = weight[player][opponent]
                if num == self.board:
                    temp *= 2
                elif num == self.choice:
                    temp *= 3
                score += temp
        
        # curr_game = self.game[self.board]
        # # most win heuristic (better than nothing)
        # for num in range(1, 10):
        #     temp = 0
        #     curr = curr_game[num]
        #     if curr > 0:
        #         if num in [1, 3, 7, 9]:
        #             temp = 10
        #         elif num in [2, 4, 6, 8]:
        #             temp = 15
        #         else:
        #             temp = 20
                
        #         if curr == 2:
        #             temp = -temp
        #         score += temp

        #     temp = 0
        #     # check rows
        #     for i in range(1, 4):
        #         j = i * 3 - 2
        #         # X . X, X X ., and . X X
        #         if self._same(curr_game, [j, j + 1]) and self._empty(curr_game, j + 2):
        #             temp += self._positive(curr_game[j]) * 30
        #         elif self._same(curr_game, [j + 1, j + 2]) and self._empty(curr_game, j):
        #             temp += self._positive(curr_game[j]) * 30
        #         elif self._same(curr_game, [j, j + 2]) and self._empty(curr_game, j + 1):
        #             temp += self._positive(curr_game[j]) * 30

        #     # check columns
        #     for i in range(1, 4):
        #         if self._same(curr_game, [i, i + 3]) and self._empty(curr_game, i + 6):
        #             temp += self._positive(curr_game[i]) * 30
        #         elif self._same(curr_game, [i + 3, i + 6]) and self._empty(curr_game, i):
        #             temp += self._positive(curr_game[i]) * 30
        #         elif self._same(curr_game, [i, i + 6]) and self._empty(curr_game, i + 3):
        #             temp += self._positive(curr_game[i]) * 30
            
        #     # check diagonals
        #     if self._same(curr_game, [1, 9]) and self._empty(curr_game, 5):
        #         temp += self._positive(curr_game[1]) * 50
        #     elif self._same(curr_game, [1, 5]) and self._empty(curr_game, 9):
        #         temp += self._positive(curr_game[1]) * 50
        #     elif self._same(curr_game, [5, 9]) and self._empty(curr_game, 1):
        #         temp += self._positive(curr_game[5]) * 50
            
        #     if self._same(curr_game, [3, 7]) and self._empty(curr_game, 5):
        #         temp += self._positive(curr_game[3]) * 50
        #     elif self._same(curr_game, [3, 5]) and self._empty(curr_game, 7):
        #         temp += self._positive(curr_game[3]) * 50
        #     elif self._same(curr_game, [5, 7]) and self._empty(curr_game, 3):
        #         temp += self._positive(curr_game[5]) * 50
        #     score += temp
        return score
