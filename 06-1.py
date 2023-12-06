pairs = [(58, 434), (81, 1041), (96, 2219), (76, 1218)]

# distance traveled == p*(t - p)
# iterate is normal method sorta

c = 1
for pair in pairs:
    k = 0

    for i in range(2, pair[0]):
        if i*(pair[0] - i) > pair[1]:
            k += 1
    
    c *= k

print(c)
