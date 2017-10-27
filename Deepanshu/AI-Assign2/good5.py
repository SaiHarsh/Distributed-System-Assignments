import random
import copy
import pdb

block_win_100 = []
block_lost_100 = []

block_win_70_1 = []
block_win_70_2 = []
block_win_70_3 = []

block_lose_70_1 = []
block_lose_70_2 = []
block_lose_70_3 = []

block_may_win_100_1 = []
block_may_win_100_2 = []
block_may_win_100_3 = []


block_may_lose_100_1 = []
block_may_lose_100_2 = []
block_may_lose_100_3 = []

block_stat = []

my_board = []
my_board_stat = []

flag = '-'
opp_flag = '-'
no_flag = '-'

is_first_move = False

class Player60:
    def __init__(self):
        # initialization
        return

    def move(self, temp_board, temp_block, old_move, flag):
        global is_first_move
        if is_first_move == False:
            initialization(flag, temp_board, temp_block)
            is_first_move = True
        if (old_move == (-1,-1)):
            update_my_config((4,4))
            return (4, 4)
        #print "+++++++++++++++++++++++++++++++++++++++"

        #print old_move
        #print flag

        best_move = minimax(old_move, temp_board, temp_block)

        #print "+++++++++++++++++++++++++++++++++++++++"
        #print best_move
        update_my_config(best_move, old_move)

        return best_move

def initialization(flag_value, board, board_stat):
    global flag, no_flag, opp_flag
    global block_win_100, block_lost_100
    global block_win_70_1, block_win_70_2, block_win_70_3,block_lose_70_1, block_lose_70_2, block_lose_70_3
    global block_may_win_100_1, block_may_win_100_2, block_may_lose_100_3,block_may_lose_100_1, block_may_lose_100_3, block_may_lose_100_3, block_stat
    global my_board, my_board_stat
    
    flag = flag_value
    no_flag = '-'
    opp_flag = 'x' if flag == 'o' else 'o'
    block_win_100 = [flag, flag, flag]
    block_lost_100 = [opp_flag, opp_flag, opp_flag]

    block_win_70_1 = [flag, flag, no_flag]
    block_win_70_2 = [flag, no_flag, flag]
    block_win_70_3 = [no_flag, flag, flag]

    block_lose_70_1 = [opp_flag, opp_flag, no_flag]
    block_lose_70_2 = [opp_flag, no_flag, opp_flag]
    block_lose_70_3 = [no_flag, opp_flag, opp_flag]

    #block_win_30 = [flag, no_flag, no_flag]
    #block_lose_30 = [opp_flag, no_flag, no_flag]

    block_may_win_100_1 = [flag, flag, opp_flag]
    block_may_win_100_2 = [flag, opp_flag, flag]
    block_may_win_100_3 = [opp_flag, flag, flag]


    block_may_lose_100_1 = [opp_flag, opp_flag, flag]
    block_may_lose_100_2 = [opp_flag, flag, opp_flag]
    block_may_lose_100_3 = [flag, opp_flag, opp_flag]

    block_stat = [
                    block_win_100, block_lost_100,
                    block_win_70_1, block_win_70_2, block_win_70_3,
                    block_lose_70_1, block_lose_70_2, block_lose_70_3,
                    block_may_win_100_1, block_may_win_100_2, block_may_lose_100_3,
                    block_may_lose_100_1, block_may_lose_100_3, block_may_lose_100_3
                ]

    my_board_stat = [row[:] for row in board_stat]

    num = 0
    block_1 = []
    block_2 = []
    block_3 = []
    for x in range(9):
        row = board[x]
        if x < 3:
            block_1[num:num+3] = row[0:3]
            block_2[num:num+3] = row[0:3]
            block_3[num:num+3] = row[0:3]
            num += 3
        
        elif x >= 3 and x < 6:
            block_1[num:num+3] = row[0:3]
            block_2[num:num+3] = row[0:3]
            block_3[num:num+3] = row[0:3]
            num += 3
        else:
            block_1[num:num+3] = row[0:3]
            block_2[num:num+3] = row[0:3]
            block_3[num:num+3] = row[0:3]
            num += 3
        if x in [2,5,8]:
            my_board.append(block_1)
            my_board.append(block_2)
            my_board.append(block_3)
            block_1 = []
            block_2 = []
            block_3 = []
            num = 0

def get_score(board, board_stat):
    #print_board(board)
    final_score = 0
    score_achieved = []
    bigscore = []

    for i in range(9):
        block = get_block(i, board)
        #print block
        for j in range(3):
            # for rows
            try:
                index = block_stat.index(block[j:j+3])
                score_achieved.append(index)
            except ValueError:
                #print block[j:j+3]
                pass
            # for columns
            try:
                index = block_stat.index(block[j::3])
                score_achieved.append(index)
            except ValueError:
                pass

        # for diagonals
        try:
            index = block_stat.index(block[0::4])
            score_achieved.append(index)
        except ValueError:
            pass
        try:
            index = block_stat.index(block[2:8:2])
            score_achieved.append(index)
        except ValueError:
            pass

    for score in score_achieved:
        if score == 0:
            final_score += 300
        elif score == 1:
            final_score += -300
        elif score == 2:
            final_score += 60
        elif score == 3:
            final_score += 70
        elif score == 4:
            final_score += 60
        elif score == 5:
            final_score += -60
        elif score == 6:
            final_score += -70
        elif score == 7:
            final_score += -60
        elif score == 8:
            final_score += -120
        elif score == 9:
            final_score += -140
        elif score == 10:
            final_score += -120
        elif score == 11:
            final_score += 120
        elif score == 12:
            final_score += 140
        elif score == 13:
            final_score += 120

    # for rows
    for k in range(3):
        try:
            index = block_stat.index(board_stat[k:k+3])
            bigscore.append(index)
        except ValueError:
            pass
    # for columns
    for k in range(3):
        try:
            index = block_stat.index(board_stat[k::3])
            bigscore.append(index)
        except ValueError:
            pass
    # for diagonals
    try:
        index = block_stat.index(board_stat[0::4])
        bigscore.append(index)
    except ValueError:
        pass
    try:
        index = block_stat.index(board_stat[2:8:2])
        bigscore.append(index)
    except ValueError:
        pass
    
    for ind in bigscore:
            if ind == 0:
                final_score += 10000
            elif ind == 1:
                final_score += -10000
            elif ind == 2:
                final_score += 2000
            elif ind == 3:
                final_score += 3000
            elif ind == 4:
                final_score += 2000
            elif ind == 5:
                final_score += -2000
            elif ind == 6:
                final_score += -3000
            elif ind == 7:
                final_score += -2000
            elif ind == 8:
                final_score += -5000
            elif ind == 9:
                final_score += -6000
            elif ind == 10:
                final_score += -5000
            elif ind == 11:
                final_score += 4500
            elif ind == 12:
                final_score += 6000
            elif ind == 13:
                final_score += 4500

    return final_score


def get_copy(board, board_stat):
    board_copy = [row[:] for row in board]
    board_stat_copy = [row[:] for row in board_stat]
    return (board_copy, board_stat_copy)

def minimax(old_move, board, board_stat):
    global flag, opp_flag, no_flag
    #print flag, opp_flag, no_flag

    allowed_blocks = get_free_and_valid_blocks(old_move, board_stat)
    cells = get_allowed_cells(allowed_blocks, board)
    best_score = float('-inf')
    best_move = cells[0]

    alpha = float('-inf')
    beta = float('inf')
    for cell in cells:
        board_copy, board_stat_copy = get_copy(board, board_stat)

        future_board = max_move(board_copy, cell)
        future_board_stat = update_board_stat(future_board, board_stat_copy, cell)
        # other player's move
        score = min_play(cell, future_board, future_board_stat, 0, alpha, beta)
        alpha = max(alpha, score)
        if score > best_score:
            best_score = score
            best_move = cell
        if beta <= alpha:
            break

    return best_move

def min_play(old_move, board, board_stat, depth, alpha, beta):
    global flag, opp_flag, no_flag
    #print "-------------------"
    #print flag, opp_flag, no_flag
    #print "-------------------"
    if (depth > 2):
        return get_score(board, board_stat)
    allowed_blocks = get_free_and_valid_blocks(old_move, board_stat)
    cells = get_allowed_cells(allowed_blocks, board)
    best_score = float('inf')

    """
    try:
        best_move = cells[0]
    except IndexError:
        print "index error"
        #pdb.set_trace()
        return get_score(board, board_stat)
    """

    for cell in cells:
        board_copy, board_stat_copy = get_copy(board, board_stat)

        future_board = min_move(board_copy, cell)
        future_board_stat = update_board_stat(future_board, board_stat_copy, cell)
        # our player's move
        score = max_play(cell, future_board, future_board_stat, depth+1, alpha, beta)
        beta = min(beta, score)
        if score < best_score:
            best_score = score
        if beta <= alpha:
            break

    return best_score

def max_play(old_move, board, board_stat, depth, alpha, beta):
    global flag, opp_flag, no_flag
    #print "********************"
    #print flag, opp_flag, no_flag
    #print "********************"
    #if (depth > 4):
    #    return get_score(board, board_stat)
    allowed_blocks = get_free_and_valid_blocks(old_move, board_stat)
    cells = get_allowed_cells(allowed_blocks, board)
    best_score = float('-inf')
    """
    try:
        best_move = cells[0]
    except IndexError:
        print "index error"
        #pdb.set_trace()
        return get_score(board, board_stat)
    """

    for cell in cells:
        board_copy, board_stat_copy = get_copy(board, board_stat)

        future_board = max_move(board_copy, cell)
        future_board_stat = update_board_stat(future_board, board_stat_copy, cell)
        score = min_play(cell, future_board, future_board_stat, depth+1, alpha, beta)
        alpha = max(alpha, score)
        if score > best_score:
            best_score = score
        if beta <= alpha:
            break

    return best_score

def max_move(board, move):
    global flag
    x = move[0]
    y = move[1]
    board[x][y] = flag
    return board


def min_move(board, move):
    global opp_flag
    x = move[0]
    y = move[1]
    board[x][y] = opp_flag
    return board

def update_my_config(move, old_move = None):
    global my_board, my_board_stat
    block_number = get_block_number(move)
    x = move[0] % 3 # vertical
    y = move[1] % 3 # horizontal
    
    index = (x*3) + y
    my_board[block_number][index] = flag

    if old_move:
        block_number = get_block_number(move)
        x = old_move[0] % 3 # vertical
        y = old_move[1] % 3 # horizontal
        
        index = (x*3) + y
        my_board[block_number][index] = opp_flag
    
    #print_my_board()


def print_my_board():
    global my_board

    for bs in my_board:
        for i in [0,3,6]: 
            print bs[i] + " " + bs[i+1] + " " + bs[i+2] 
        print 


def get_my_block(block_number):
    global my_board
    return my_board[block_number]

def update_board_stat(board, board_stat, move):
    # update board stat 
    #print move
    block_number = get_block_number(move)
    #print block_number
    block = get_block(block_number, board)
    #print_block(block)
    #print_board_stat(board_stat)

    board_stat_new = [ row[:] for row in board_stat ]

    new_flag = 0
    for i in range(9) :
            if block[i] == '-' :
                new_flag = 1
    

    if block[0:3] == ['x', 'x', 'x' ] or block[3:6] == ['x', 'x', 'x' ] or block[6:9] == ['x', 'x', 'x' ] or block[0::3] == ['x', 'x', 'x' ] or block[3::6] == ['x', 'x', 'x' ] or block[6::9] == ['x', 'x', 'x' ] or block[0::4] == ['x', 'x', 'x' ] or block[2:7:2] == ['x', 'x', 'x' ] :
        board_stat_new[block_number] = 'x'

    elif block[0:3] == ['o', 'o', 'o' ] or block[3:6] == ['o', 'o', 'o' ] or block[6:9] == ['o', 'o', 'o' ] or block[0::3] == ['o', 'o', 'o' ] or block[3::6] == ['o', 'o', 'o' ] or block[6::9] == ['o', 'o', 'o' ] or block[0::4] == ['o', 'o', 'o' ] or block[2:7:2] == ['o', 'o', 'o' ] :
        board_stat_new[block_number] = 'o'
    
    elif new_flag == 1 :
            board_stat_new[block_number] = '-'
    else:
        board_stat_new[block_number] = 'D'

    #print_board_stat(board_stat_new)

    return board_stat_new


def get_block_number(move):
    x = move[0]
    y = move[1]
    if x < 3 and y < 3:
        return 0
    elif x < 3 and (y>=3 and y<6):
        return 1
    elif x < 3 and (y>=6 and y<9):
        return 2

    elif x < 6 and y < 3:
        return 3
    elif x < 6 and (y>=3 and y<6):
        return 4
    elif x < 6 and (y>=6 and y<9):
        return 5

    elif x < 9 and y < 3:
        return 6
    elif x < 9 and (y>=3 and y<6):
        return 7
    elif x < 9 and (y>=6 and y<9):
        return 8

                 

def print_board_stat(bs):
    print "=========== Block Status NEW========="
    for i in range(0, 9, 3): 
        print bs[i] + " " + bs[i+1] + " " + bs[i+2] 
    print "=================================="
    print


def print_board(gb):
    print '=========== Board ====================='
    for i in range(9):
        if i > 0 and i % 3 == 0:
                print
        for j in range(9):
                if j > 0 and j % 3 == 0:
                        print " " + gb[i][j],
                else:
                        print gb[i][j],

        print
    print "========================================"

def print_block_by_number(block_number, board):
    x = (block_number / 3) * 3
    y = (block_number % 3) * 3
    print "================BLOCK================="
    for i in range(3):
        print board[x+i][y] + " " + board[x+i][y+1] + " " + board[x+i][y+2]
    print "================BLOCK================="

def print_block(block):
    print "================BLOCK================="    
    for i in range(3):
        print block[i*3] + " " + block[i*3+1] + " " + block[i*3+2]
    print "======================================"


def is_allowed_block(block_number, temp_block):
    return temp_board[block_number] == '-'

def get_block(block_number, board):
    block = []
    x = (block_number / 3) * 3
    y = (block_number % 3) * 3
    
    for i in range(3):
        for j in range(3):
            block.append(board[x+i][y+j])
    
    #print_block(block)
    return block

def get_free_and_valid_blocks(old_move, game_stat):
    valid_blocks = get_valid_blocks(old_move)
    #print "**********************"
    #print valid_blocks
    #print game_stat
    #print "**********************"
    free_and_valid_blocks = []

    for block in valid_blocks:
        if game_stat[block] == '-':
            free_and_valid_blocks.append(block)

    if len(free_and_valid_blocks) == 0:
        for block_pos in range(9):
            if game_stat[block_pos] == '-':
                free_and_valid_blocks.append(block_pos)

    return free_and_valid_blocks
     

def get_valid_blocks(old_move):
    # first-move
    if old_move[0] < 0 and old_move[1] < 0:
        return [i for i in range(9)]

    x = old_move[0] % 3 # vertical
    y = old_move[1] % 3 # horizontal
    # upper
    if x == 0 and y == 0:
        # left
        return [1, 3]
    elif x == 0 and y == 1:
        # middle
        return [0, 2]
    elif x == 0 and y == 2:
        # right
        return [1, 5]
    
    # middle
    elif x == 1 and y == 0:
        # left
        return [0, 6]
    elif x == 1 and y == 1:
        # middle
        return [4]
    elif x == 1 and y == 2:
        # right
        return [2, 8]
    
    # lower
    elif x == 2 and y == 0:
        # left
        return [3, 7]
    elif x == 2 and y == 1:
        # middle
        return [6, 8]
    elif x == 2 and y == 2:
        # right
        return [5, 7]

def is_empty_cell(cell, block):
    index = (cell[0]*3) + cell[1]
    return block[index] == '-'

def get_allowed_cells(blocks, board):
    #print blocks
    allowed_cells = []
    for block in blocks:
        block_stat = get_block(block, board)
        for i in range(3):
            for j in range(3):
                if is_empty_cell((i,j), block_stat):
                    #print "Got the move " + str(i) + ", " + str(j)
                    allowed_cells.append((i + (block/3)*3, j + (block%3)*3))

    return allowed_cells

