



sum = 0
user = 'IX'
roman = {'I' : 1,"V":5,
        "X":10,
        "L":50,
        "C":100,
        "D":500,
        "M":1000}

for idx,u in enumerate(user):
    if idx+1<len(user) and roman[u] < roman[user[idx+1]]:
        sum -= roman[u]
    
    else:
        sum += roman[u]


print(sum)
