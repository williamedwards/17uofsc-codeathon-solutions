#!/usr/bin/python3

# Representation
# Tuple (x, y, z, type)
#   x, y: coords on grid, zero index from top left
#   z: level 0 index
#   type in {unwalkable, walkable, entry point, staircase, warp point, pikachu}

import heapq

# Define Constants
NOWALK = 0
WALK = 1
ENTER = 2
STAIR = 3
WARP = 4
PIKACHU = 5

INF = 1000

num_levels = int(input())
level_dims = [int(val) for val in input().split(" ")]

# We will represent tuple (tentative distance, type)
# We can just compute one level at a time
for level_dim in level_dims:
    input() # Read blank line
    grid = []
    entry_coords = None
    dest_coords = None # Stairs or pikachu
    warp_coords = []

    total_path_length = 0
    for i in range(level_dim):
        row = []
        for j, char in enumerate(input()):
            if char == "#":
                row.append((False, NOWALK, INF))
            if char == " ":
                row.append((False, WALK, INF))
            if char == "s":
                row.append((False, STAIR, INF))
                dest_coords = (i, j)
            if char == "p":
                row.append((False, PIKACHU, INF))
                dest_coords = (i, j)
            if char == "e":
                row.append((False, ENTER, INF))
                entry_coords = (i, j)
            if char == "w":
                row.append((False, WARP, INF))
                warp_coords.append([i, j])
        grid.append(row)
    unvisited = [(0, entry_coords[0], entry_coords[1])]
    while True:
        current = heapq.heappop(unvisited)
        grid_square = grid[current[1]][current[2]]
        if(grid_square[0]):
            # This has already been visited
            continue
        grid[current[1]][current[2]] = \
            (True, grid_square[1], grid_square[2])
        if(grid_square[1] == STAIR or grid_square[1] == PIKACHU):
            total_path_length += current[0]
            break
        # Check adjacent squares
        for xoff, yoff in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
            if current[1] + xoff < 0 or current[2] + yoff < 0:
                continue
            try:
                other_grid_square = \
                    grid[current[1] + xoff][current[2] + yoff]
                if other_grid_square[1] == NOWALK:
                    continue
                if current[0] + 1 < other_grid_square[2]:
                    grid[current[1] + xoff][current[2] + yoff] = (
                        other_grid_square[0],
                        other_grid_square[1],
                        current[0] + 1)
                    heapq.heappush(
                        unvisited, (current[0] + 1,
                                    current[1] + xoff,
                                    current[2] + yoff))
            except IndexError:
                continue
        # Check for warp points
        if grid_square[1] == WARP:
            warp_point = warp_coords[0]
            if (current[1], current[2]) == warp_point:
                warp_point = warp_coords[1]
            other_grid_square = grid[warp_point[0]][warp_point[1]]
            if current[0] + 1 < other_grid_square[0]:
                other_grid_square[0] = current[0] + 1
                heapq.heappush(
                    unvisited, (other_grid_square[0],
                                warp_point[0],
                                warp_point[1]))
print(total_path_length+1)

