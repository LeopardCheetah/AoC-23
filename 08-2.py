'''
# do some encoding

def encode(s):
    c = 0
    # add first digit
    c += 10000*(ord(s[0]) - ord('A') + 1)
    c += 100*(ord(s[1]) - ord('A') + 1)
    c += (ord(s[2]) - ord('A') + 1)
    return c

def bins(ls, val):
    # assuming val exists
    left = 0
    right = len(ls) - 1
    while left < right:
        mid = (left + right)//2
        if ls[mid] == val:
            return mid
        
        if ls[mid] > val:
            # aka gotta move to the left more
            right = mid - 1
            continue
        
        if ls[mid] < val:
            # aka gotta make mid higher
            left = mid + 1
            continue
    
    return left # since left == right



steps = input().strip()
blank = input()

ls = []
for _ in range(758):
    # encode everything
    # A --> 1, AA --> 100 + 1, AAA --> 10000 + 100 + 1

    x = input().strip()

    # print(x[:3],end=' ') -- start
    # print(x[7:10]) -- left
    # print(x[12:15]) -- right
    
    start_node = x[:3]
    left = x[7:10]
    right = x[12:15]

    # encode
    ls.append((encode(start_node), encode(left), encode(right)))


ls.sort()
first_vals = [pair[0] for pair in ls] # binsearch this list

node_at = encode("SBA")
ind = bins(first_vals, node_at)
pointer = 0
step_count = 0

points_hit = []

while len(points_hit) < 10: # ZZZ
    if node_at % 100 == 26:
        points_hit.append(step_count)
    
    # get new node
    if pointer == len(steps):
        pointer = 0
        # easy

    
    if steps[pointer] == 'L':
        # take a left
        # next node is at ls[prev_ind][1]
        node_at = ls[ind][1]
        ind = bins(first_vals, node_at)
    
    if steps[pointer] == 'R':
        node_at = ls[ind][2]
        ind = bins(first_vals, node_at)

    pointer += 1
    step_count += 1

print(points_hit)
'''
# AAA, BFA, DFA, XFA, QJA, SBA

# for AAA, ls = [18023, 36046, 54069, 72092, 90115, 108138, 126161, 144184, 162207, 180230]
# for BFA, ls = [19637, 39274, 58911, 78548, 98185, 117822, 137459, 157096, 176733, 196370]
# for DFA, ls = [21251, 42502, 63753, 85004, 106255, 127506, 148757, 170008, 191259, 212510]
# for XFA, ls = [16409, 32818, 49227, 65636, 82045, 98454, 114863, 131272, 147681, 164090]
# for QJA, ls = [11567, 23134, 34701, 46268, 57835, 69402, 80969, 92536, 104103, 115670]
# for SBA, ls = [14257, 28514, 42771, 57028, 71285, 85542, 99799, 114056, 128313, 142570]

# lcm(ab)*gcd(ab) = ab


def gcd(a, b):
    while(b):
        a, b = b, a % b
    return a

def lcm(a, b):
    return a*b//gcd(a, b)

print(lcm(lcm(18023, 19637), lcm(21251, 16409)))
print(lcm(11567, 14257))

print(lcm(6340257101, 613051))
