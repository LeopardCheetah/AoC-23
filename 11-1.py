ls = []

for _ in range(140):
    ls.append(list(input().strip()))

h = []

for i in range(140):
    for j in range(140):
        if ls[i][j] == '#':
            h.append((i, j))


rows = []
columns = []

for i in range(140):
    if ls[i].count('#') == 0:
        rows.append(i)
    

for i in range(140):
    f = True
    c = 0
    while f and c < 140:
        if ls[c][i] == '#':
            f = False
            break
        
        c += 1
    
    if f:
        columns.append(i)

r = 0
for one in range(len(h)):
    for two in range(one + 1, len(h)):
        # check 
        a = (min(h[one][0], h[two][0]), min(h[one][1], h[two][1]))
        b = (max(h[one][0], h[two][0]), max(h[one][1], h[two][1]))

        # a << b
        r += b[0] - a[0] + b[1] - a[1]
        for n in rows:
            if a[0] < n < b[0]:
                r += 1
        
        for n in columns:
            if a[1] < n < b[1]:
                r += 1

print(r)
# 11.1
