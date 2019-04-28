
class State:
    # game is a copy of the entire board
    # current_board tracks which board we are in
    # choice is the move we choose
    def __init__(self, game, current_board, choice):
        self.game = game
        self.board = current_board
        self.choice = choice

    def human(self):
        print('B{}C{}'.format(self.board, self.choice))

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
            if curr_game[start] == curr_game[start + 1] == curr_game[start + 2]:
                return curr_game[start]

        # check columns
        for i in range(1, 4):
            if curr_game[i] == curr_game[i + 3] == curr_game[i + 6]:
                return curr_game[i]
        
        # check diagonals
        if curr_game[1] == curr_game[5] == curr_game[9]:
            return curr_game[1]
        if curr_game[3] == curr_game[5] == curr_game[7]:
            return curr_game[3]

        # no wins
        return win
