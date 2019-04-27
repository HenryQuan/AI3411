'''
Tree and Node class for generating the entire game map
'''

from debug import *
import random, math

<<<<<<< HEAD
class Tree:
    def __init__(self):
        # give default values
        self.children = []
        self.heuristic = 0
        self.number = 0
        self.parent = None

    '''
    mode is either True or False (Max or Min)
    '''
    # minimax with alpha-beta pruning
    def minimax_ab(self, root, alphabeta, mode=True):
        # debug_print('H{}B{}'.format(root.heuristic, root.number))
        if len(root.children) == 0:
            return root.get_heuristic()

        # try something else
        if mode:
            best_move = 0
            best = -math.inf
            for node in root.children:
                choice = self.minimax_ab(node, alphabeta, False)
                if choice == 1: debug_print('win')
                if choice > best:
                    best = choice
                    best_move = node.number
                
                alphabeta[0] = max(alphabeta[0], choice)
                if alphabeta[1] <= alphabeta[0]:
                    break
            return best            
        else:
            best_move = 0
            worst = math.inf
            for node in root.children:
                choice = self.minimax_ab(node, alphabeta, True)
                if choice == -1: debug_print('good')
                if choice < worst:
                    worst = choice
                    best_move = node.number
                alphabeta[1] = min(alphabeta[1], choice)
                if alphabeta[1] <= alphabeta[0]:
                    break              
            return worst

    # print the entire tree
    def print_tree(self):
        debug_print('------')
        if len(self.children) > 0:
            for i in self.children:
                i.print_node()
        debug_print('------')

=======
>>>>>>> f947b9dcb26ea241339ff7470aa7f4209eab0228
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