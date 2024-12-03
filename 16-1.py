# day 16, 110 by 110 grid

grid = []
for _ in range(110):
    grid.append(input().strip())


def new_coords(row, col, orientation):
    if orientation == 'L':
        return row, col - 1
    
    if orientation == 'R':
        return row, col + 1
    
    if orientation == 'U':
        return row - 1, col
    
    if orientation == 'D':
        return row + 1, col
    
    return "????"




left_energy = [[0 for _ in range(110)] for a in range(110)] # this is all based on orientation
up_energy = [[0 for _ in range(110)] for a in range(110)]
right_energy = [[0 for _ in range(110)] for a in range(110)]
down_energy = [[0 for _ in range(110)] for a in range(110)]

queue = [] # should be pairs for location and also heading

queue.append((0, 0, 'R')) # start!


while len(queue) > 0:
    # ehrm there are things to do

    
    # take the first thing in the queue, then "advance" it one step
    # ok first find location
    pair = queue.pop() 

    if pair[0] < 0 or pair[0] > 109:
        # ehrm
        continue # dw about it
    
    if pair[1] < 0 or pair[1] > 109:
        continue # again


    # if item exists cut it
    if pair[2] == 'L' and left_energy[pair[0]][pair[1]] == 1:
        continue
    
    if pair[2] == 'U' and up_energy[pair[0]][pair[1]] == 1:
        continue

    if pair[2] == 'D' and down_energy[pair[0]][pair[1]] == 1:
        continue


    if pair[2] == 'R' and right_energy[pair[0]][pair[1]] == 1:
        continue
        




    item_at_location = grid[pair[0]][pair[1]]


    if pair[2] == 'L':
        left_energy[pair[0]][pair[1]] = 1
    
    if pair[2] == 'D':
        down_energy[pair[0]][pair[1]] = 1
    
    if pair[2] == 'U':
        up_energy[pair[0]][pair[1]] = 1
    
    if pair[2] == 'R':
        right_energy[pair[0]][pair[1]] = 1



    if item_at_location == '.':
        # just keep going where you were going
        a, b = new_coords(pair[0], pair[1], pair[2])

        queue.append((a, b, pair[2])) # orientation is constant
        continue

    if (item_at_location == '-' and (pair[2] == 'L' or pair[2] == 'R')):
        # we vibe
        a, b = new_coords(pair[0], pair[1], pair[2])
        queue.append((a, b, pair[2])) 
        continue
    
    if (item_at_location == '|' and (pair[2] == 'U' or pair[2] == 'D')):
        a, b = new_coords(pair[0], pair[1], pair[2])
        queue.append((a, b, pair[2])) 
        continue

    # ok time to deal with the "/\"s, then the splitters
    if item_at_location == '\\':
        if pair[2] == 'U':
            # you are now left
            a, b = new_coords(pair[0], pair[1], 'L')
            queue.append((a, b, 'L'))
            continue
        
        if pair[2] == 'L':
            # up
            a, b = new_coords(pair[0], pair[1], 'U')
            queue.append((a, b, 'U'))
            continue
        
        if pair[2] == 'D':
            # you are now right
            a, b = new_coords(pair[0], pair[1], 'R')
            queue.append((a, b, 'R'))
            continue
        
        if pair[2] == 'R':
            a, b = new_coords(pair[0], pair[1], 'D')
            queue.append((a, b, 'D'))
            continue
        
        # don't be here
        continue
    

    if item_at_location == '/':
        if pair[2] == 'U':
            # you are now right
            a, b = new_coords(pair[0], pair[1], 'R')
            queue.append((a, b, 'R'))
            continue
        
        if pair[2] == 'R':
            # up
            a, b = new_coords(pair[0], pair[1], 'U')
            queue.append((a, b, 'U'))
            continue
        
        if pair[2] == 'D':
            a, b = new_coords(pair[0], pair[1], 'L')
            queue.append((a, b, 'L'))
            continue
        
        if pair[2] == 'L':
            a, b = new_coords(pair[0], pair[1], 'D')
            queue.append((a, b, 'D'))
            continue
        
        # don't be here (again)
        continue
    
    # ok deal with the annoying splitters
    if item_at_location == '|':
        # implied that you are going left/right into one of these bad bois
        # basically now go up and down from here

        a, b = new_coords(pair[0], pair[1], 'U')
        queue.append((a, b, 'U'))
        
        c, d = new_coords(pair[0], pair[1], 'D')
        queue.append((c, d, 'D'))
        continue
    
    # implied that it's up/down hitting a "-"
    a, b = new_coords(pair[0], pair[1], 'L')
    queue.append((a, b, 'L'))
    
    c, d = new_coords(pair[0], pair[1], 'R')
    queue.append((c, d, 'R'))
    continue


# mega-list

mega_list = [[max(left_energy[i][j], right_energy[i][j], up_energy[i][j], down_energy[i][j]) for j in range(110)] for i in range(110)]


for row in mega_list:
    for item in row:
        print(item, end='')
    
    print()


total_sum = 0
for row in mega_list:
    total_sum += sum(row)

print(total_sum)
