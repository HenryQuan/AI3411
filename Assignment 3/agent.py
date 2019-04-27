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
import sys, copy
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
min_depth = 2
max_depth = 20
# this is only for fun
player_name = 'Henry\'s OP Bot'

# get the optimal depth to search
def adapative_depth(moves):
    depth = min_depth
    debug_print('\nMoves: {}'.format(moves))
    depth += math.floor(moves / 81 * (max_depth - min_depth))
    return int(depth)

# check if there is a winner 
def check_win(game, board):
    win = 0
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

def copy_game(game):
    return copy.deepcopy(game)

'''
game, board and number are the state
depth limits the search
node is the current node
max_player (max or min)
'''
# build a tree from current game with a depth limit
def minimax_ab(node, game, board, alphabeta, max_player, depth):
    # depth reached 0 or game ends (player or opponent won)
    if depth == 0 or check_win(game, board):
        return
    
    for num in range(1, 10):
        new_game = copy_game(game)
        # illegal moves
        if new_game[board][num] > 0:
            continue

        # place the move
        if max_player:
            new_game[board][num] = 1
        else:
            new_game[board][num] = 2

        win = check_win(new_game, board)
        
        new_node = Node(node, new_game, num, not max_player)
        node.children.append(new_node)
        minimax_ab(new_node, new_game, num, alphabeta, not max_player, depth - 1)

    # if max_player:
    #     # Max
    #     max_value = -math.inf

    #     for child in node.children:
    #         value = minimax_ab(child, )
    # else:
    #     # Min
    #     min_value = -math.inf

# do some magic and get the best move
def optimal_move():
    # build a tree with a good depth
    depth = adapative_depth(moves)
    debug_print('Depth: {}'.format(depth))

    # find best move
    root = Node(None, copy_game(game_boards), curr_board, True)
    minimax_ab(root, copy_game(game_boards), curr_board, [-math.inf, math.inf], True, depth)
    root.print_node()
    best_move = best_node.board
    debug_print('Best -> {}'.format(best_move))
    return best_move

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