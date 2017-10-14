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

def is_position_winnable(board):
    # Check to see if we have isolated empty space.
    for i in range(8): # Iterate over columns
        seen_empty = False
        for j in reversed(range(5)):
            if not board[j][i]:
                seen_empty = True
            elif seen_empty:
                return False
    return True

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
    print(new_block)
    for y in range(6):
        if(in_board(new_block, p, y)
           and not collides_with_existing_blocks(board, new_block, p, y)):
            has_found_valid_pos = True
        else:
            if has_found_valid_pos:
                y = y - 1
                print(y)
                for elem in new_block:
                    print(elem)
                    print(p + elem[0], y - elem[1])
                    new_board[y - elem[1]][p + elem[0]] = True
                return new_board
    return None


