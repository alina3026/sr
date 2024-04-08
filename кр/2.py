import csv
import json

sp = []
d = {}
with open('witches.csv') as in_file:
    reader = csv.DictReader(in_file, delimiter=';')
    for line in reader:
        sp.append((line['witch'], line['transform']))
    for elem in sp:
        if elem[0] in d:
            d[elem[0]].append(elem[1])
        else:
            d[elem[0]] = [elem[1]]
    for val, key in d.items():
        key.sort()
    with open('wizardry.json', 'w') as out_file:
        json.dump(d, out_file, ensure_ascii=False, indent=4)
