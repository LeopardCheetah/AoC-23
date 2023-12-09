def val(string):
    k = len(string) - 1
    c = 0
    s = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    for i in string:
        c += 26**k*s.index(i)
        k -= 1
    
    return c


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

print()
steps = 0
now = m[0]


while now[0] != 17575:
    # R or L?
    # steps % len(path)


    if path[steps % len(path)] == 'R':
        # go right
        ind = find(m, now[2])
        now = m[ind]
    else:
        ind = find(m, now[1])
        now = m[ind]

    
    steps += 1

print('answer:', steps)
