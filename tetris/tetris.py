# Representation of board. 2-d list of bools.  Outer list is rows.  False is empty, true is filled


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
        print(width)

        # Compute the rotation
        for j, elem in enumerate(new_block):
            new_x = elem[1]
            new_y = width - elem[0]
            new_block[j] = (new_x, new_y)
    return new_block

# Apply move.  Return board if legal; return None otherwise
def apply_move(board, block_type, r, p):
    pass

