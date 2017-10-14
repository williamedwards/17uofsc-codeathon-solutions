# Representation of board. 2-d list of bools.  Outer list is rows.  False is empty, true is filled


import copy
# Block types compute as offset from lower left-hand corner
BLOCK_TYPES = {
    "i" : [(0, 0), (1, 0), (2, 0), (3, 0)],
    "j" : [(0, 0), (1, 0), (2, 0), (0, 1)],
    "t" : [(0, 0), (1, 0), (2, 0), (1, 1)],
    "s" : [(0, 0), (1, 0), (1, 1), (2, 1)],
    "z" : [(1, 0), (2, 0), (0, 1), (1, 1)],
    "o" : [(0, 0), (1, 0), (0, 1), (1, 1)]
}

#def is_position_winnable(board):
#    # Check to see if we have isolated empty space.
#    for i in range(8): # Iterate over columns
#        seen_empty = False
#        for j in reversed(range(5)):
#            if not board[j][i]:
#                seen_empty = True
#            elif seen_empty:
#                return False
#    return True

# Returns: board with cleared rows
def do_clear(board):
    did_clear = False
    new_board = copy.deepcopy(board)
    for i, row in reversed(list(enumerate(new_board))):
        if row == [True] * 8:
            did_clear = True
            del new_board[i]
    while len(new_board) < 5:
        new_board = [[False] * 8] + new_board
    if did_clear:
        return do_clear(new_board)
    else:
        return new_board

def rotate_block(block, r):
    new_block = block[:]
    for i in range(r):
        # Get width
        width = 0
        for elem in new_block:
            if elem[0] > width:
                width = elem[0]

        # Compute the rotation
        for j, elem in enumerate(new_block):
            new_x = elem[1]
            new_y = width - elem[0]
            new_block[j] = (new_x, new_y)
    return new_block

def in_board(block, x, y):
    for elem in block:
        if x + elem[0] < 0 or x + elem[0] > 7:
            return False
        if y - elem[1] < 0 or y - elem[0] > 4:
            return False
    return True

def collides_with_existing_blocks(board, block, x, y):
    for elem in block:
        if board[y - elem[1]][x + elem[0]]:
            return True
    return False

# Apply move.  Return board if legal; return None otherwise
def apply_move(board, block, r, p):
    new_board = copy.deepcopy(board)
    new_block = rotate_block(block, r)
    has_found_valid_pos = False
    for y in range(6):
        if(in_board(new_block, p, y)
           and not collides_with_existing_blocks(board, new_block, p, y)):
            has_found_valid_pos = True
        else:
            if has_found_valid_pos:
                y = y - 1
                for elem in new_block:
                    new_board[y - elem[1]][p + elem[0]] = True
                return new_board
    return None

def find_move_sequence(board, blocks):
    if blocks == []:
        if do_clear(board) == [[False] * 8] * 5:
            return []
        else:
            return None
    for p in range(7):
        for r in range(4):
            new_board = apply_move(board, blocks[0], r, p)
            if not new_board is None:
                rem_seq = find_move_sequence(new_board, blocks[1:])
                if rem_seq is not None:
                    return [(r, p)] + rem_seq
    return None

