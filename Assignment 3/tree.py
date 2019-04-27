'''
Tree and Node class for generating the entire game map
'''

from debug import *
import random, math

class Node:
    # board is not saved but only for calculating heuristic
    def __init__(self, parent, max_player, game, board, num):
        self.number = num
        self.parent = parent
        self.max_player = max_player

        self.game = game
        self.board = board

        self.children = []

    # This node and its children
    def print_node(self):
        debug_print('B{}N{}'.format(self.board, self.number))
        for i in self.children:
            i.print_node()

    # get heuristic of this move
    def get_heuristic(self):
        # check if player wins
        win = self._check_win(self.game, self.board, self.player, self.number)
        # win -> 1, lose -> 2, no wins or draw -> 0
        if win == 1:
            # debug_print('win')
            return 1
        elif win == 2:
            # debug_print('lose')
            return -1
        else:
            return 0

    # if player or opponent wins
    def _check_win(self, game, board, player, num):
        win = 0

        if player:
            game[board][num] = 1
        else:
            game[board][num] = 2

        curr = game[board]

        # check rows
        for i in range(1, 4):
            start = i * 3 - 2
            if curr[start] == curr[start + 1] == curr[start + 2]:
                return curr[start]

        # check columns
        for i in range(1, 4):
            if curr[i] == curr[i + 3] == curr[i + 6]:
                return curr[i]
        
        # check diagonals
        if curr[1] == curr[5] == curr[9]:
            return curr[1]
        if curr[3] == curr[5] == curr[7]:
            return curr[3]

        # no wins
        return win
