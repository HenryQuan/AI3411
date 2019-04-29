#!/usr/bin/python3

'''
COMP3411 19T1
Assignment 3 Nine-board Tic-Tac-Toe
Yiheng Quan Z5098268

I checked Zac senpai's starter code and got some ideas about what's going on.
My current solution to use minimax and alpha-beta pruning. Gradually increas ethe depth when the game is closer to an end.

The heuristic function will be measuring 'most wins' and the cost is always one for all moves.
'''

import socket
import random, math
import sys, copy as COPY
# some modules to help this
from node import Node
from debug import debug_print
from state import State

'''
9x9 board
0 - Empty
1 - Player
2 - Opponent
'''
# easy index (don't need to worry about -1)
game_boards = [[0] * 10 for i in range(10)]
moves = 1
player = 1
last_move = 0
curr_board = 0

# set the max/min depth we can reach (free feel to adjust these two values)
min_depth = 5
max_depth = 10
# this is only for fun
player_name = 'Stupid Henry'

# get the optimal depth to search
def adapative_depth(moves):
    depth = min_depth
    debug_print('\nMoves: {}'.format(moves))
    depth += math.floor(moves / 81 * (max_depth - min_depth))
    return int(depth)

# make a copy of current game board
def copy(game):
    return COPY.deepcopy(game)

# consider optimal play
def minimax(node, max_player, alpha, beta, depth):
    # depth reached or game ended
    curr_state = node.state.current_state()
    if curr_state > 0 or depth == 0:
        return node.state.get_score()

    # max or min depending on max_player
    for choice in range(1, 10):
        new_node = node.new_node(choice)
        if new_node == None:
            # already taken
            continue
        node.children.append(new_node)

    best_value = -math.inf if max_player else math.inf
    for child in node.children:
        curr_value = minimax(child, not max_player, alpha, beta, depth - 1)
        if max_player:
            best_value = max(curr_value, best_value)
            alpha = max(alpha, curr_value)
            # beta cut
            if beta <= alpha:
                break       
        else:
            best_value = min(curr_value, best_value)
            beta = min(beta, curr_value)
            # alpha cut
            if beta <= alpha:
                break
    return best_value          

# do some magic and get the best move
def optimal_move():
    # build a tree with a good depth
    depth = adapative_depth(moves)
    debug_print('Depth: {}'.format(depth))
    debug_print('Board: {}'.format(curr_board))

    # max 9 possible choices and pick the best one
    all_choices = []
    for choice in range(1, 10):
        if game_boards[curr_board][choice] > 0:
            # already taken
            continue
        
        new_board = copy(game_boards)
        new_board[curr_board][choice] = 1
        node = Node(None, State(new_board, curr_board, choice, 1), True)
        curr_value = minimax(node, False, -math.inf, math.inf, depth - 1)
        all_choices.append([choice, curr_value])

    debug_print(all_choices)
    best_moves = []
    max_value = -math.inf
    for pair in all_choices:
        max_value = max(pair[1], max_value)
    for pair in all_choices:        
        if pair[1] == max_value:
            best_moves.append(pair[0])

    last = random.choice(best_moves)
    debug_print('{} -> {}'.format(last, best_moves))
    return last

# get a random move
def dummy_move():
    n = random.randint(1, 9)
    while not game_boards[curr_board][n] == 0:
        n = random.randint(1, 9)
    return n

# visualise (X, O instead of 1, 2 and 0)
def print_player(i):
    if i > 2:
        return '.'
    if player == 1:
        return ['.', 'X', 'O'][i]
    else:
        return ['.', 'O', 'X'][i]

# print a row (modified from Zac senpai's code)
def print_row(board, a, b, c, i, j, k):
    # The marking script doesn't seem to like this either, so just take it out to submit
    print("", print_player(board[a][i]), print_player(board[a][j]), print_player(board[a][k]), end = " | ")
    print(print_player(board[b][i]), print_player(board[b][j]), print_player(board[b][k]), end = " | ")
    print(print_player(board[c][i]), print_player(board[c][j]), print_player(board[c][k]))

# Print the entire board (modified from Zac senpai's code)
def print_board(board):
    print_row(board, 1,2,3,1,2,3)
    print_row(board, 1,2,3,4,5,6)
    print_row(board, 1,2,3,7,8,9)
    print(" ------+-------+------")
    print_row(board, 4,5,6,1,2,3)
    print_row(board, 4,5,6,4,5,6)
    print_row(board, 4,5,6,7,8,9)
    print(" ------+-------+------")
    print_row(board, 7,8,9,1,2,3)
    print_row(board, 7,8,9,4,5,6)
    print_row(board, 7,8,9,7,8,9)
    print()

# choose a move to play (modified from Zac senpai's code)
def play():
    # random move
    # n = dummy_move()

    # get the best move
    n = optimal_move()
    place(curr_board, n, 1)
    return n

# place a move in the global boards (modified from Zac senpai's code)
def place(board, num, player):
    global curr_board, moves, last_move
    curr_board = num
    last_move = board
    game_boards[board][num] = player
    moves += 1
    print_board(game_boards)

# Parse command from server (modified from Zac senpai's code)
def parse(string):
    if '(' in string:
        command, args = string.split('(')
        args = args.split(')')[0]
        args = args.split(',')
    else:
        command, args = string, []
    
    global player_name, player
    if command == 'second_move':
        player_name += ' O'
        player = 2
        place(int(args[0]), int(args[1]), 2)
        return play()
    elif command == 'third_move':
        player_name += ' X'
        player = 1
        # place the move that was generated for us
        place(int(args[0]), int(args[1]), 1)
        # place opponent's last move
        place(curr_board, int(args[2]), 2)
        return play()
    elif command == 'next_move':
        place(curr_board, int(args[0]), 2)
        return play()
    elif command == 'win':
        print('{} wins :)\n'.format(player_name))
        return -1
    elif command == 'loss':
        return -1
    return 0

# Setup socket and keep receiving commands (modified from Zac senpai's code)
def main():
    if len(sys.argv) < 3 or (len(sys.argv) > 2 and not sys.argv[1] == '-p'):
        # some basic validations
        print('Usage: ./agent.py -p (port)')
        sys.exit(1)

    port = int(sys.argv[2])
    address = 'localhost'
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # it takes a while for the server to go down and free the port
    try:
        s.connect((address, port))

        while True:
            text = s.recv(1024).decode()
            if not text:
                continue
            for line in text.split('\n'):
                response = parse(line)
                # game is over
                if response < 0:
                    return
                elif response > 0:
                    s.sendall((str(response) + '\n').encode())
    except socket.error as e:
        # if you connect to the same port too frequent
        print('cannot connect : %s'.format(e))
    finally:
        s.close()
    
if __name__ == '__main__':
    main()