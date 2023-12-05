seeds = input().strip().split()

seeds = [int(seeds[a]) for a in range(1, len(seeds))]


mega = []

num = [45, 20, 26, 39, 44, 36, 11]

for j in range(7):
    lts = []
    x = input()
    x = input()
    for _ in range(num[j]):
        a, b, c = map(int, input().strip().split())

        lts.append((a, b, c))
    
    mega.append(lts)

m = 10**15
# transformation time or something
for num in seeds:
    n = num
    for ls in mega:
        # this is each step
        for pair in ls:
            # mapping!
            # if in range
            if pair[1] <= n and pair[1] + pair[2] > n:
                n = pair[0] + n - pair[1]
                break
    
    m = min(m, n)

print(m)
