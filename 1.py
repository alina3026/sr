counts = {}
with open('gloss.txt', 'r') as f:
    n = f.readline()
    for elem in n:
        counts[elem] = counts.get(elem, 0) + 1

s = sorted(counts.items(), key=lambda x: x[1])
print(s)
# min_value = min(counts.values())
# sp = []
# for x in s:
#     if x[1] == min_value:
#         sp.append(x[0])
# sp.sort()
# print(sp[-1])