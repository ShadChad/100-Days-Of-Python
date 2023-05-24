

for a in range(1,100):
    for b in range(1,100):
        c = (a**2 + b**2) ** 0.5
        if c == int(c) and c<99:
            print(a,b,int(c))


# for a in range(1,10y