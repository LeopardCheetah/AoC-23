cards = [1]*186

for ind in range(186):
    card = input().strip()

    parse = card[10:]
    
    nums = parse.split()
    # looks like 10 numbers first (scratch card) then my numbers

    lso = nums[:10]
    lst = nums[10:]

    k = 0

    for i in lso:
        if i in lst:
            k += 1
    
    # k = number of matches on your card
    # card ind + 1, ind + 2, all the way until ind + k += 1

    for i in range(1, k+1):
        cards[ind + i] += cards[ind]

print(sum(cards))
