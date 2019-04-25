class Tree:
    # board is not saved but only for calculating heuristic
    def __init__(board, num, self):
        self.number = num
        self.heuristic = self._get_heuristic(board, num)

    # get heuristic of this move
    def _get_heuristic(board, num, self):
        # check for win first
        return 0