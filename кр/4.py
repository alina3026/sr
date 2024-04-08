import csv
import sqlite3

name = input()
category = input()
kind = int(input())
sp = [['id', 'idea', 'name', 'kindness']]

con = sqlite3.connect(name)
cur = con.cursor()
id_cat = cur.execute(f"""SELECT id FROM Categories WHERE type = '{category}'""").fetchall()[0][0]
res = cur.execute(f'SELECT * FROM Ideas WHERE category_id = {id_cat} and kindness > {kind - 1}').fetchall()
con.commit()
con.close()
print(res)
for line in res:
    sp.append([line[0], line[2], line[1], line[4]])
print(sp)
with open('think_n_do.csv', 'w', newline='', encoding="utf8") as f:
    writer = csv.writer(f, delimiter=',', quoting=csv.QUOTE_MINIMAL)
    for line in sp:
        writer.writerow(line)
    # with open('files/квадраты.csv', 'w', newline='', encoding="utf8") as csvfile:
    #     writer = csv.writer(
    #         csvfile, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    #     for i in range(10):
    #         writer.writerow([i, i ** 2, "Квадрат числа %d равен %d" % (i, i ** 2)])
