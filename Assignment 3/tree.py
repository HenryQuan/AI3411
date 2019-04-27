'''
Node class for saving game state
'''

from debug import *

class Node:
    def __init__(self, parent, game, board, max_player):
        self.parent = parent
        # game state
        self.game = game
        self.board = board
        # more moves
        self.children = []

    # This node and its children
    def print_node(self):
        debug_print('B{} - {}'.format(self.board, self.game[self.board]))
        for i in self.children:
            i.print_node()
