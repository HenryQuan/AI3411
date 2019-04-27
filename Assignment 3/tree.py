'''
Tree and Node class for generating the entire game map
'''

from debug import *
import random, math

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
        if len(root.children) == 0 or not root.heuristic == 0:
            return root.heuristic

        # try something else
        if mode:
            best_move = 0
            best = -math.inf
            for node in root.children:
                choice = self.minimax_ab(node, alphabeta, False)
                if choice > best:
                    best = choice
                    best_move = node.number
                
                alphabeta[0] = max(alphabeta[0], choice)
                if alphabeta[1] <= alphabeta[0]:
                    break
            return best_move            
        else:
            best_move = 0
            worst = math.inf
            for node in root.children:
                choice = self.minimax_ab(node, alphabeta, True)
                if choice < worst:
                    worst = choice
                    best_move = node.number
                alphabeta[1] = min(alphabeta[1], choice)
                if alphabeta[1] <= alphabeta[0]:
                    break              
            return best_move

    # print the entire tree
    def print_tree(self):
        debug_print('------')
        if len(self.children) > 0:
            for i in self.children:
                i.print_node()
        debug_print('------')

class Node:
    # board is not saved but only for calculating heuristic
    def __init__(self, parent, player, board, num):
        self.number = num
        self.parent = parent
        self.player = player
        self.heuristic = self._get_heuristic(board, num)
        self.children = []

    # This node and its children
    def print_node(self):
        debug_print('H{}N{}'.format(self.heuristic, self.number))
        for i in self.children:
            i.print_node()

    # get heuristic of this move
    def _get_heuristic(self, board, num):
        # check if player wins
        win = self._check_win(board, num)
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
    def _check_win(self, board, num):
        win = 0

        # check rows
        for i in range(1, 4):
            start = i * 3 - 2
            if board[start] == board[start + 1] == board[start + 2]:
                return board[start]

        # check columns
        for i in range(1, 4):
            if board[i] == board[i + 3] == board[i + 6]:
                return board[i]
        
        # check diagonals
        if board[1] == board[5] == board[9]:
            return board[1]
        if board[3] == board[5] == board[7]:
            return board[3]

        # no wins
        return win
