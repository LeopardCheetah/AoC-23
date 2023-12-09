c = 0

for _ in range(200):
    ls = [int(a) for a in input().split()]

    # extrapolate next value
    # essentailly just keep on making adj matrices that add up and up and up

    extrapolate = []

    extrapolate.append(ls)

    f = True

    while f:
        lst = extrapolate[-1]
        lsf = [lst[i+1] - lst[i] for i in range(len(lst) - 1)]

        if lsf == [0]*len(lsf):
            f = False
        
        extrapolate.append(lsf)
    
    k = 0
    extrapolate = extrapolate[::-1]
    for l in extrapolate:
        k = l[0] - k

    c += k
    
print(c)
