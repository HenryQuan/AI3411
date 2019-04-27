'''
Tree and Node class for generating the entire game map
'''

from debug import *
import random, math

class Node:
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
    def get_score(self):
        # check if player wins
        win = self._check_win(self.game, self.board, self.max_player, self.number)
        # win -> 1, lose -> 2, no wins or draw -> 0
        if win == 1:
            # debug_print('win')
            return 1
        elif win == 2:
            # debug_print('lose')
            return -1
        else:
            return 0