s = 'XII'
sum = 0

dict = {'I' : 1,"V":5,
        "X":10,
        "L":50,
        "C":100,
        "D":500,
        "M":1000}
# i = 0
# for i in range(len(s)):
#     if i+1<len(s) and dict[s[i]]< dict[s[i+1]]:
#         sum -= dict[s[i]]
#     else:
#         sum +=dict[s[i]]
# print(sum)

i = 0
for z in s:
    if i+1<len(s) and dict[s[i]]<dict[s[i+1]]:
        sum -= dict[s[i]]
    else:
        sum+= dict[s[i]]
    i += 1
print(sum)
