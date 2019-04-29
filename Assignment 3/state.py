
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

    def get_score(self, curr_state):
        if curr_state == 1:
            return 100
        elif curr_state == 2:
            return -100
        else:
            score = 0
            # add heuristic
            for num in self.game[self.choice]:
                temp = 0
                curr = self.game[self.choice][num]
                if curr > 0:
                    # most win
                    if curr in [1, 3, 7, 9]:
                        temp = 3
                    elif curr in [2, 4, 6, 8]:
                        temp = 2
                    else:
                        temp = 4

                    if curr == 2:
                        temp *= -1
                score += temp
            return score

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
