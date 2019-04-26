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
import sys, gc
from tree import * 
from debug import *

'''
9x9 board
0 - Empty
1 - Player
2 - Opponent
'''
# easy index (don't need to worry about -1)
game_boards = [[0] * 10 for i in range(10)]
moves = 1
curr_board = 0

# set the max/min depth we can reach (free feel to adjust these two values)
min_depth = 5
max_depth = 20
# this is only for fun
player_name = 'Henry\'s OP Bot'

# get the optimal depth to search
def adapative_depth(moves):
    depth = min_depth
    debug_print('\nMoves: {}'.format(moves))
    depth = depth + math.floor(moves / 81 * (max_depth - min_depth))
    return int(depth)

'''
root -> Tree or Node
board -> current board
player -> player(1) or opponent(2)
curr_depth -> number
max_depth -> number
'''
# build a tree from current game with a depth limit
def build_tree(root, board, player, curr_depth, max_depth):
    # termination
    if (curr_depth > max_depth):
        return

    # loop through all possible situation
    for num in range(1, 10):
        # must be zero (illegal move otherwise)
        illegal_move = game_boards[board][num] > 0
        if illegal_move:
            # debug_print('{}-{} is illegal'.format(board, num))
            continue

        # build tree recursively
        curr = Node(root, game_boards[board], num, player)
        build_tree(curr, num, not player, curr_depth + 1, max_depth)
        root.children.append(curr)
        

# do some magic and get the best move
def optimal_move():
    # build a tree with a good depth
    depth = adapative_depth(moves)
    debug_print('Depth: {}'.format(depth))
    debug_print('Board: {}'.format(curr_board))
    root = Tree()
    # build a new tree and search through it
    build_tree(root, curr_board, True, 1, 1)
    root.print_tree()

    best = root.minimax_ab(root, [-math.inf, math.inf])
    debug_print('Best -> {}-{}'.format(curr_board, best))
    gc.collect()
    return best

# get a random move
def dummy_move():
    n = random.randint(1, 9)
    while not game_boards[curr_board][n] == 0:
        n = random.randint(1, 9)
    return n

# print a row (modified from Zac senpai's code)
def print_row(board, a, b, c, i, j, k):
    # The marking script doesn't seem to like this either, so just take it out to submit
    print("", board[a][i], board[a][j], board[a][k], end = " | ")
    print(board[b][i], board[b][j], board[b][k], end = " | ")
    print(board[c][i], board[c][j], board[c][k])

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
    global curr_board, moves
    curr_board = num
    moves += 1
    game_boards[board][num] = player

# Parse command from server (modified from Zac senpai's code)
def parse(string):
    if '(' in string:
        command, args = string.split('(')
        args = args.split(')')[0]
        args = args.split(',')
    else:
        command, args = string, []
    
    global player_name
    if command == 'second_move':
        player_name += ' O'
        place(int(args[0]), int(args[1]), 2)
        return play()
    elif command == 'third_move':
        player_name += ' X'
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