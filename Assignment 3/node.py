'''
Node class for saving game state
'''

from debug import *
from state import *

class Node:
    def __init__(self, parent, game, board, choice, max_player):
        self.parent = parent
        # game state
        self.state = State(game, board, choice)
        self.max_player = max_player
        # more moves
        self.children = []

    # This node and its children
    def print_node(self):
        self.state.human()
        for i in self.children:
            i.print_node()
