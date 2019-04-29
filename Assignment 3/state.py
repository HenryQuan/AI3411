
import copy

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
        win = self.current_state()
        if win == 1:
            return 1000
        elif win == 2:
            return -1000
        else:
            return self._heuristic()

    def new_state(self, new_choice, player):
        if self.game[self.choice][new_choice] > 0:
            # illegal
            return None
        # copy current board and place new choice
        new_game = copy.deepcopy(self.game)
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
        curr_game = self.game[self.board]

        # most win heuristic (better than nothing)
        for num in range(1, 10):
            curr = curr_game[num]
            temp = 0
            if curr > 0:
                if num in [1, 3, 7, 9]:
                    temp = 75
                elif num in [2, 4, 6, 8]:
                    temp = 50
                else:
                    temp = 100
                
                if curr == 2:
                    temp = -temp
            score += temp

        # # check rows
        # for i in range(1, 4):
        #     j = i * 3 - 2
        #     # X . X, X X ., and . X X
        #     if self._same(curr_game, [j, j + 1]) and self._empty(curr_game, j + 2):
        #         score += self._positive(curr_game[j]) * 100
        #     elif self._same(curr_game, [j + 1, j + 2]) and self._empty(curr_game, j):
        #         score += self._positive(curr_game[j]) * 100
        #     elif self._same(curr_game, [j, j + 2]) and self._empty(curr_game, j + 1):
        #         score += self._positive(curr_game[j]) * 50

        # # check columns
        # for i in range(1, 4):
        #     if self._same(curr_game, [i, i + 3]) and self._empty(curr_game, i + 6):
        #         score += self._positive(curr_game[i]) * 100
        #     elif self._same(curr_game, [i + 3, i + 6]) and self._empty(curr_game, i):
        #         score += self._positive(curr_game[i]) * 100
        #     elif self._same(curr_game, [i, i + 6]) and self._empty(curr_game, i + 3):
        #         score += self._positive(curr_game[i]) * 50
        
        # # check diagonals
        # if self._same(curr_game, [1, 9]) and self._empty(curr_game, 5):
        #     score += self._positive(curr_game[1]) * 100
        # elif self._same(curr_game, [1, 5]) and self._empty(curr_game, 9):
        #     score += self._positive(curr_game[1]) * 200
        # elif self._same(curr_game, [5, 9]) and self._empty(curr_game, 1):
        #     score += self._positive(curr_game[5]) * 200
        
        # if self._same(curr_game, [3, 7]) and self._empty(curr_game, 5):
        #     score += self._positive(curr_game[3]) * 100
        # elif self._same(curr_game, [3, 5]) and self._empty(curr_game, 7):
        #     score += self._positive(curr_game[3]) * 200
        # elif self._same(curr_game, [5, 7]) and self._empty(curr_game, 3):
        #     score += self._positive(curr_game[5]) * 200

        return score
