'''
Node class for saving game state
'''

from debug import debug_print
from state import State

class Node:
    def __init__(self, parent, state, max_player):
        self.parent = parent
        # game state
        self.state = state
        self.max_player = max_player
        # more moves
        self.children = []


    # get a new node with one depth deeper
    def new_node(self, new_choice):
        new_state = self.state.new_state(new_choice, 2 if self.max_player else 1)
        if new_state == None:
            return None
        return Node(self, new_state, not self.max_player)

    # This node and its children
    def print_node(self):
        self.state.human()
        for i in self.children:
            i.print_node()
