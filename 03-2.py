# adjacent to a symbol
# parse numbers first then figure out the symbol thing???

# 140 by 140 input grid
ls = []
for _ in range(140):
    ls.append(list(input().strip()))

# isolate a string then look up/down


def trace(a, b):
    # given that a, b might be in the middle we have to trace on either end
    global ls

    s = ''
    # add chars in one by one
    s += str(ls[a][b])

    c, d = a, b
    numbers = [str(i) for i in range(10)]

    d += 1
    mid = 0
    while d < 140 and ls[c][d] in numbers:
        mid += 1
        s += ls[c][d]
        d += 1
    
    d = b - 1
    while d > -1 and ls[c][d] in numbers:
        s = ls[c][d] + s 
        d -= 1
    
    # integer is now here
    # find length
    length_int = len(s)
    s = int(s)

    return s, length_int - 1 - mid, mid # number, how many chars left, how many chars right 

    # now parse it from length or something



run = ''
start = (0, 0)
j = 0
for row in range(len(ls)):
    for ind in range(len(ls[0])): 
        if ls[row][ind] != '*':
            continue
        
        # we now have a star bois
        # take a look at left, right, up, down for numbers - if there's a number then trace it

        # take a look left and right first
        c = 1
        count = 0

        numbers = [str(i) for i in range(10)]

        if ind != 0:
            if ls[row][ind - 1] in numbers:
                count += 1
                c *= int(trace(row, ind-1)[0])
        
        if ind != 139:
            if ls[row][ind + 1] in numbers:
                count += 1
                c *= int(trace(row, ind + 1)[0])
        
        # now look up/down

        if row != 0:
            # top left = row - 1, ind - 1
            # top right = row - 1, ind + 1

            # process by cases
            # ..., 1.., ..1, .1., .11, 111, 11., 1.1

            # edge case ind = 139 not covered

            # not my fondest code
            if ls[row - 1][ind - 1] in numbers and ls[row - 1][ind + 1] in numbers and ls[row - 1][ind] in numbers:
                c *= int(trace(row - 1, ind)[0])
                count += 1
            elif ls[row - 1][ind] in numbers and (ls[row - 1][ind + 1] in numbers or ls[row - 1][ind - 1] in numbers):
                c *= int(trace(row - 1, ind)[0])
                count += 1
            elif ls[row - 1][ind - 1] in numbers and ls[row - 1][ind + 1] in numbers:
                c *= int(trace(row - 1, ind - 1)[0])
                count += 1
                c *= int(trace(row - 1, ind + 1)[0])
                count += 1
            elif ls[row - 1][ind + 1] in numbers:
                c *= int(trace(row - 1, ind + 1)[0])
                count += 1
            elif ls[row - 1][ind - 1] in numbers:
                c *= int(trace(row - 1, ind - 1)[0])
                count += 1
            elif ls[row - 1][ind] in numbers:
                c *= int(ls[row - 1][ind])
                count += 1

        if row != 139:
            if ls[row + 1][ind + 1] in numbers and ls[row + 1][ind + 1] in numbers and ls[row + 1][ind] in numbers:
                c *= int(trace(row + 1, ind)[0])
                count += 1
            elif ls[row + 1][ind] in numbers and (ls[row + 1][ind + 1] in numbers or ls[row + 1][ind - 1] in numbers):
                c *= int(trace(row + 1, ind)[0])
                count += 1
            elif ls[row + 1][ind - 1] in numbers and ls[row + 1][ind + 1] in numbers:
                c *= int(trace(row + 1, ind - 1)[0])
                count += 1
                count += 1
                c *= int(trace(row + 1, ind + 1)[0])
            elif ls[row + 1][ind + 1] in numbers:
                c *= int(trace(row + 1, ind + 1)[0])
                count += 1
            elif ls[row + 1][ind - 1] in numbers:
                c *= int(trace(row + 1, ind - 1)[0])
                count += 1
            elif ls[row + 1][ind] in numbers:
                c *= int(ls[row + 1][ind])
                count += 1
        
        if count == 2:
            j += int(c)


        


print(j)
