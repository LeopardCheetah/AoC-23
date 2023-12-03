def s(line):
    # id, r, g, b

    ls = line.split(';')
    lst = ls[0].split(':')

    lsf = lst + ls[1:]

    n = int(lsf[0][5:])
    r, g, b = 0, 0, 0


    for i in range(len(lsf)):
        if i == 0:
            continue

        lss = lsf[i].split()

        # finally done preprocessing

        some = [1, 3, 5]

        for index in some:
            try:
                if lss[index] == 'green' or lss[index] == 'green,':
                    g = max(g, int(lss[index-1]))

                if lss[index] == 'red' or lss[index] == 'red,':
                    r = max(r, int(lss[index-1]))
                
                if lss[index] == 'blue' or lss[index] == 'blue,':
                    b = max(b, int(lss[index-1]))
            except:
                continue
    
    return n, r, g, b

# a
def parse(line):
    n, r, g, b = s(line)
    if r < 13 and g < 14 and b < 15:
        return n
    
    return 0
    
# b
def p(line):
    n, r, g, b = s(line)
    return r*g*b


c = 0
for _ in range(100):
    l = input().strip()

    c += p(l)


print(c)
