# adjacent to a symbol
# parse numbers first then figure out the symbol thing???

# 140 by 140 input grid
ls = []
for _ in range(140):
    ls.append(list(input().strip()))

# isolate a string then look up/down


run = ''
start = (0, 0)
j = 0
for row in range(len(ls)):
    for ind in range(len(ls[0])): 
        if ord('0') <= ord(ls[row][ind]) <= ord('9'):
            if run == '':
                start = (row, ind)

            run += ls[row][ind]
            # note: ls[k] is a string
            continue
        
        if run == '':
            continue
        
        # validate cells and add to sum
        l = len(str(run))
        run = int(run)

        # now figure out the cells touching
        # cells of it are start, start + 1, start + 2, ...., start + l - 1

        # cells touching are (a, b - 1), (a, b+l) and everything with a-1 and a+1

        a = start[0]
        b = start[1]

        n = ['.'] + [str(i) for i in range(10)]

        switch = False

        if a != 0:
            # check row up
            for c in range(l + 2):
                # a, b - 1 + c
                if b - 1 + c > 139:
                    continue

                if ls[a-1][b-1+c] not in n:
                    switch = True
                    break
        
        if a != 139 and not switch:
            # check down
            for c in range(l + 2):

                if b - 1 + c > 139:
                    continue
                
                if a + 1 > 139:
                    continue

                if ls[a+1][b-1+c] not in n:
                    switch = True
                    break

        if b != 0 and not switch:
            switch = (ls[a][b-1] not in n)

        if b != 139 and not switch:
            if b + l > 139:
                pass
            else:
                switch = (ls[a][b+l] not in n)

        if switch:
            j += run
        
        run = ''
        start = (0, 0)

print(j)
