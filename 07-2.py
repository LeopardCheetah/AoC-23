def pairs(x):
    c = 0
    k = list(x)

    for i in range(4):
        if k[i] == k[i+1]:
            c += 1
    
    return c


def rankk(x):
    y = list(x)
    y.sort()
    p = pairs(y)

    if x.count('J') == 4:
        return 7
    
    # 3, 2, 1 jokers
    # 4 of a kind == 3 jokers, diff types

    if x.count('J') == 3:
        # check if they're different
        if y[4] == 'J':
            if y[0] == y[1]:
                return 7
            
            return 6
        
        if y[0] == 'J':
            if y[3] == y[4]:
                return 7
            
            return 6
        
        if y[0] == y[4]:
            return 7
        
        return 6
    


    if x.count('J') == 2:
        # case JJABC
        # case JJAAA
        # case JJAAB

        if (x.count(y[0]) == 2 and x.count(y[4]) == 3) or (x.count(y[0]) == 3 and x.count(y[4]) == 2):
            return 7
        
        # case JJABC
        # case JJAAB

        if p == 2:
            return 6
        
        # case JJABC
        return 4
        # no full house
    
    # x.count() == 1

    # JABCD
    # JAABC
    # JAAAB
    # JAAAA
    # JAABB

    if p == 0:
        return 2
    
    if p == 1:
        return 4 
    
    # JAAAB
    # JAAAA
    # JAABB

    if p == 2 and (x.count(y[0]) == 3 or x.count(y[1]) == 3 or x.count(y[2]) == 3):
        # JAAAB
        return 6
    
    if p == 2:
        return 5
    
    return 7















def rank(x):
    if x.count('J') > 0:
        return rankk(x)
    y = list(x)
    y.sort()
    p = pairs(y)

    if p == 4:
        return 7
    
    if x.count(y[0]) == 4 or x.count(y[1]) == 4:
        return 6
    
    # full house
    if p == 3:
        return 5
    
    # three of a kind
    if y[0] == y[1] == y[2] or y[3] == y[1] == y[2] or y[4] == y[3] == y[2]:
        return 4
    
    if p == 2:
        return 3
    
    if p == 1:
        return 2
    
    return 1


def comp(x, y):
    a = rank(x)
    b = rank(y)

    if a > b:
        return x
    
    if b > a:
        return y
    
    r = 'AKQT98765432J'

    for i in range(5):
        if x[i] == y[i]:
            continue
        
        if r.index(x[i]) < r.index(y[i]):
            return x
        
        return y
    
    return -1



def sort(array):
    
  # loop to access each array element
    for i in range(len(array)):

        # loop to compare array elements
        for j in range(0, len(array) - i - 1):

            # compare two adjacent elements
            # change > to < to sort in descending order
            if comp(array[j], array[j+1]) == array[j]:
                array[j], array[j+1] = array[j+1], array[j]

    return array


ls = []
lst = []
for i in range(1000):
    a, b = input().split()

    ls.append(a)
    ls.append(int(b))
    lst.append(a)

sorte = sort(lst)

c = 0
for j in range(1000):
    c += (j+1)*ls[(ls.index(lst[j]) + 1)]

print(c)


