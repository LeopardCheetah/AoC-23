def val(string):
    k = len(string) - 1
    c = 0
    s = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'

    for i in string:
        c += 40**k*s.index(i)
        k -= 1

        # if k == -1 and i == 'A':
        #    print(string)
    
    return c


start_two = [0, 1800, 5000, 37000, 25960, 28840]
end = [2145, 41025, 19465, 2025, 29545, 31065] # XXZs

def find(ls, value):
    v = value

    left = 0
    right = len(ls) - 1

    while left < right:
        mid = (left + right)//2

        if ls[mid][0] > v:
            # too big -> decrease right
            right = mid - 1
            continue

        if ls[mid][0] < v:
            left = mid + 1
            continue
        
        return mid
    
    return left



path = input().strip()
buf = input()

m = []
for _ in range(758):
    ls = input().split()


    # m.append((ls[0], ls[2][1:-1], ls[3][:-1]))
    m.append((val(ls[0]), val(ls[2][1:-1]), val(ls[3][:-1])))
    continue

m.sort()


start = []
for num in start_two:
    start.append(m[find(m, num)])


steps = 0
now = start.copy()


f = True
while f:
    # R or L?
    # steps % len(path)
    lst = []

    if path[steps % len(path)] == 'R':
        for item in now:
            # go right
            lst.append(m[find(m, item[2])])
    else:
        for item in now:
            lst.append(m[find(m, item[1])])


    steps += 1

    # checker function for f

    f = False
    for pair in lst:
        if pair[0] not in end:
            f = True
            break
    
    now = lst.copy()


print('answer:', steps)
