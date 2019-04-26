'''
Tree and Node class for generating the entire game map
'''

from debug import *
import random

class Tree:
    def __init__(self):
        # give default values
        self.children = []
        self.heuristic = 0
        self.number = 0

    '''
    mode is either True or False (Max or Min)
    '''
    # minimax with alpha-beta pruning
    def minimax_ab(self, root, mode=True):
        # debug_print('H:{} N:{}'.format(root.heuristic, root.number))
        if len(root.children) == 0:
            return root.heuristic

        # try something else
        if mode:
            best_move = []
            best = -9999
            for node in root.children:
                choice = self.minimax_ab(node, False)
                # debug_print(choice)
                if (choice >= best):
                    best = choice
                    best_move.append(node.number)
            return best_move            
        else:
            best_move = []
            worst = 9999
            for node in root.children:
                choice = self.minimax_ab(node, True)
                # debug_print(choice)
                if (choice <= worst):
                    worst = choice
                    best_move.append(node.number)
            return best_move

    # print the entire tree
    def print_tree(self):
        debug_print('------')
        if (len(self.children) > 0):
            for i in self.children:
                i.print_node()
        debug_print('------')

class Node:
    # board is not saved but only for calculating heuristic
    def __init__(self, parent, board, num, player):
        self.number = num
        self.parent = parent

        if player:
            # player
            self.player = 1
        else:
            # opponent
            self.player = 2

        self.heuristic = self._get_heuristic(board, num)
        self.children = []

    # This node and its children
    def print_node(self):
        debug_print('B: {} H: {}'.format(self.number, self.heuristic))
        for i in self.children:
            i.print_node()

    # get heuristic of this move
    def _get_heuristic(self, board, num):
        # check if player wins
        win = self._check_win(board, num)
        weight = 0
        if win == 1:
            weight = 99
        elif win == 2:
            weight = -99
        else:
            # most-win heuristic
            if num == 5:
                weight = 4
            if num in [1, 3, 7, 9]:
                weight = 3
            elif num in [2, 4, 6, 8]:
                weight = 2 

        # calculate overall heuristic        
    # if self.player == 1:
        weight += self.parent.heuristic
    # else: 
        # weight -= self.parent.heuristic

        return weight

    # if player or opponent wins
    def _check_win(self, board, num):
        win = 0
        # place the new move
        new_board = board[:]
        new_board[num] = 1

        # check rows
        for i in range(1, 3):
            start = i * 3 - 2
            if new_board[start] == new_board[start + 1] == new_board[start + 2]:
                return new_board[start]

        # check columns
        for i in range(1, 3):
            if new_board[i] == new_board[i + 3] == new_board[i + 6]:
                return new_board[i]
        
        # check diagonals
        if new_board[1] == new_board[5] == new_board[9]:
            return new_board[1]
        if new_board[3] == new_board[5] == new_board[7]:
            return new_board[3]

        # no wins
        return win
