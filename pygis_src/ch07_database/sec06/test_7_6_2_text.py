# -*- coding: utf-8 -*-

import shutil
import sqlite3 as sqlite

shutil.copy("./gdata/test-2.3.sqlite", './gdata/xx_db_kz.sqlite')
conn = sqlite.connect('./gdata/xx_db_kz.sqlite')

conn.enable_load_extension(True)
conn.execute('SELECT load_extension("mod_spatialite.so.7")')
cur = conn.cursor()

cvs_text = '''Author,Book,Lang,Category,Price
"Alighieri, Dante",Divina commedia,Italian,Literature,"12,50"
"Alighieri, Dante",Divina commedia,中国,Literature,"12,50"
"Alighieri, Dante",Divina commedia,Italian,Literature,"12,50"
"Alighieri, Dante",Divina commedia,Italian,Literature,"12,50"'''

with open('xx_out.txt', 'w') as fo:
    fo.write(cvs_text)
#

sql = "CREATE VIRTUAL TABLE books USING VirtualText(xx_out.txt, utf8, 1, COMMA, DOUBLEQUOTE, ',');"
cur.execute(sql)
cur.execute('PRAGMA table_info(books)')
[print(rec) for rec in cur]

sql2 = "SELECT * FROM books ORDER BY Lang, Author limit 5"
cur.execute(sql2)
[print(rec) for rec in cur]

sql = '''SELECT Book, Author FROM Books
     WHERE Category = 'Literature' AND Price < 10 AND Lang =
    'English'; '''
cur.execute(sql)
[print(rec) for rec in cur]
