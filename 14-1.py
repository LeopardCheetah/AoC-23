# 100x100 grid

grid = []
size = 100
for _ in range(size):
    grid.append(input().strip())

# access using grid[i][j]



# roll everything up
# ok well the Os will just collapse up into nothing

new_grid = [[0 for _ in range(size)] for a in range(size)] # only gonna track circular rocks


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
            # rock
            # move it to pointer + 1
            pointer = row + 1 
            continue
        
    # we good?


s = 0
c = size
for row in new_grid:
    s += c*sum(row)
    c -= 1

print(s)
