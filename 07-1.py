def pairs(x):
    c = 0
    k = list(x)

    for i in range(4):
        if k[i] == k[i+1]:
            c += 1
    
    return c

def rank(x):
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
    
    r = 'AKQJT98765432'

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
    print((ls.index(lst[j]) + 1))
    c += (j+1)*ls[(ls.index(lst[j]) + 1)]

print(c)



