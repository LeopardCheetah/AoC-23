# 100x100 grid

g = []
size = 100
for _ in range(size):
    g.append(input().strip())

# access using grid[i][j]



# roll everything up
# ok well the Os will just collapse up into nothing
def roll_north(grid):
    new_grid = [[-1 for _ in range(size)] for a in range(size)] # only gonna track circular rocks


    for col in range(size):
        # focus on the [i][col_ind] tiles

        pointer = 0 # i = 0

        for row in range(size):
            if grid[row][col] == '.':
                # we chill
                continue
            
            if grid[row][col] == 'O':
                new_grid[pointer][col] = 1
                pointer += 1
                # we vibe
                continue
            
            if grid[row][col] == '#':
                new_grid[row][col] = 0
                # rock
                # move it to pointer + 1
                pointer = row + 1 
                continue
            
        # we good?


    # convert back to dots and dashes
    for i in range(size):
        for j in range(size):
            if new_grid[i][j] == -1:
                new_grid[i][j] = "."
                continue
            
            if new_grid[i][j] == 0:
                new_grid[i][j] = "#"
                continue
            
            new_grid[i][j] = "O"
    
    return new_grid


def rotate_right(grid):
    # grid is size by size
    # make west now the new "North"

    new_grid = [["." for _ in range(size)] for a in range(size)]

    # (0, 0) --> (0, 9)
    # (0, 1) --> (1, 9)
    # (1, 0) --> (0, 8)
    # (1, 1) --> (1, 8)
    # (a, b) --> (b, 9 - a)
    # (9-b, a) --> (a, b)

    for i in range(size):
        for j in range(size):
            new_grid[i][j] = grid[size - j - 1][i]
    
    return new_grid



def spin_cycle(grid):
    # roll + rotate x4

    new_grid = grid.copy()
    for _ in range(4):
        rolled_grid = roll_north(new_grid)
        rotated_grid = rotate_right(rolled_grid)
        new_grid = rotated_grid.copy()
    
    return new_grid
    

list_of_grids = [g]
for ttt in range(200):
    
    spun_grid = spin_cycle(g)


    s = 0
    c = size
    for row in spun_grid:
        cr = 0
        for item in row:
            if item == 'O':
                cr += 1
        s += c*cr
        c -= 1

    print(ttt + 1, "sum =", s)

    #for row in spun_grid:
    #    for thing in row:
     #       print(thing,end='')
     #   
      #  print()
    

    if spun_grid in list_of_grids:
        print("!! duplicate !!")
        print(list_of_grids.index(spun_grid), ttt + 1)
        break
    else:
        list_of_grids.append(spun_grid)
        
    g = spun_grid.copy()
