import csv
import sqlite3

name = input()
result_input = input()
class_input = int(input())
sp = [['id', 'location', 'test', 'examiner', 'class']]

con = sqlite3.connect(name)
cur = con.cursor()
result_ok = cur.execute(f'SELECT * FROM Tests WHERE result = "{result_input}"').fetchall()
check_class = cur.execute(f'SELECT * FROM Examiners WHERE class >= {class_input}').fetchall()
id_class_ok = cur.execute(f'SELECT id FROM Examiners WHERE class >= {class_input}').fetchall()
con.commit()
con.close()
id_class_ok2 = []
for elem in id_class_ok:
    id_class_ok2.append(elem[0])
# print(result_ok)

for line in result_ok:
    if line[3] in id_class_ok2:
        sp.append([line[0], line[1], line[2], line[3]])
# print(sp)

for line in sp:
    for elem in check_class:
        if elem[0] == line[3]:
            line[3] = elem[1]
            line.append(elem[2])


# print(sp)
with open('landing.csv', 'w', newline='', encoding="utf8") as f:
    writer = csv.writer(f, delimiter=';', quoting=csv.QUOTE_MINIMAL)
    for line in sp:
        # print(line)
        writer.writerow(line)

