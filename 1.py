counts = {}
with open('gloss.txt', 'r') as f:
    n = f.readline()
    for elem in n:
        counts[elem] = counts.get(elem, 0) + 1

s = sorted(counts.items(), key=lambda x: x[1])
max_value = max(counts.values())
sp = []
for x in s:
    if x[1] != max_value:
        sp.append((x[0], x[1]))
max_value2 = []
sp2 = []
for elem in sp:
    max_value2.append(elem[1])
max_value2_ = max(max_value2)
for x, y in sp:
    if y == max_value2_:
        sp2.append(x)
sp2.sort()
print(sp2[0])
