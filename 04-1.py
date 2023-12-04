#4.1
c = 0

for _ in range(186):
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
    
    if k == 1:
        c += 1
        continue
    
    if k == 0:
        continue
    
    c += 2**(k-1)

print(c)
