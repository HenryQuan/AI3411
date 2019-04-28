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
player = 1
last_move = 0
curr_board = 0

# set the max/min depth we can reach (free feel to adjust these two values)
min_depth = 3
max_depth = 3
# this is only for fun
player_name = 'Stupid Henry'

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

def get_score(game, board):
    win = check_win(game, board)
    if win == 1:
        return 100
    elif win == 2:
        return -100
    else:
        score = 0
        # for num in range(1, 10):
        #     temp = 0
        #     curr = game[board][num]
        #     if curr > 0:
        #         if num in [1, 3, 7, 9]:
        #             temp = 3
        #         elif num in [2, 4, 6, 8]:
        #             temp = 2
        #         else:
        #             temp = 4

        #         if curr == 2:
        #             temp *= -1
        #         score += temp
        return score

def copy_game(game):
    return copy.deepcopy(game)

'''
game, board and number are the state
depth limits the search
node is the current node
max_player (max or min)
'''
# build a tree from current game with a depth limit
def minimax_ab(node, game, board, number, alpha, beta, max_player, depth):
    win = check_win(game, board)
    if win > 0 or depth == 0:
        return get_score(game, board)
        
    # build tree and then get min or max
    if max_player:
        max_score = -math.inf
        for num in range(1, 10):
            # illegal moves
            if game[number][num] > 0:
                continue

            # place move
            new_game = copy_game(game)
            new_game[number][num] = 1
            # save this state
            new_node = Node(node, new_game, num, True)
            curr = minimax_ab(new_node, new_game, number, num, alpha, beta, not max_player, depth - 1)
            max_score = max(max_score, curr)
            # alpha = max(alpha, curr)
            # if beta <= alpha:
            #     break
        return max_score
    else:
        min_score = math.inf
        for num in range(1, 10):
            # illegal moves
            if game[number][num] > 0:
                continue

            # place move
            new_game = copy_game(game)
            new_game[number][num] = 2
            # save this state
            new_node = Node(node, new_game, num, False)
            curr = minimax_ab(new_node, new_game, number, num, alpha, beta, not max_player, depth - 1)
            min_score = min(min_score, curr)
            # beta = min(beta, curr)
            # if beta <= alpha:
            #     break 
        return min_score

# do some magic and get the best move
def optimal_move():
    # build a tree with a good depth
    depth = adapative_depth(moves)
    debug_print('Depth: {}'.format(depth))

    # find best move
    root = Node(None, copy_game(game_boards), curr_board, True)
    optimal_move = minimax_ab(root, game_boards, last_move, curr_board, math.inf, -math.inf, True, depth - 1)

    # root.print_node()
    debug_print(optimal_move)
    # best_moves = []
    # max_score = -math.inf
    # for t in all_moves:
    #     max_score = max(max_score, t[0])
    # for t in all_moves:
    #     if t[0] == max_score:
    #         best_moves.append(t[1])
    # choice = random.choice(best_moves)
    # debug_print('-> {}'.format(choice))
    return dummy_move()

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
    # print_board(game_boards)

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