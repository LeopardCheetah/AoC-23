# day one

def find_num(s):
    for i in range(len(s)):
        if ord('0') <= ord(s[i]) <= ord('9'):
            return (i, int(s[i]))


# part two

r = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
m = [j[::-1] for j in r]

def find_n_ls(s, ls):
    w = ls.copy()

    ind, v = map(int, find_num(s))


    for i in range(len(w)):
        k = s.find(w[i])

        if k > -1 and k < ind:
            v = i + 1
            ind = k
    
    return v


su = 0
for i in range(1000):
    s = input().strip()

    su += 10*find_n_ls(s, r) + find_n_ls(s[::-1], m)

print(su)
