# -*- coding: utf-8 -*-
import os
import shutil
import sqlite3 as sqlite


shutil.copy("gdata/test-2.3.sqlite", 'gdata/xx_new_db.sqlite')

conn = sqlite.connect('gdata/xx_new_db.sqlite')

conn.enable_load_extension(True)
conn.execute('SELECT load_extension("mod_spatialite.so.7")')
cur = conn.cursor()

print('=' * 20)
sql = 'SELECT count(*) FROM Towns'
cur.execute(sql)
print(cur.fetchone()[0])

print('=' * 30)
del_sql = 'DELETE FROM Towns WHERE peoples < 100000'
cur.execute(del_sql)
sql = 'SELECT count(*) FROM Towns'
cur.execute(sql)
print(cur.fetchone()[0])

conn.rollback ()

sql = 'SELECT count(*) FROM Towns'
cur.execute(sql)
print(cur.fetchone()[0])

print('=' * 30)


del_sql = 'DELETE FROM Towns WHERE peoples < 100000'
cur.execute(del_sql)
sql = 'SELECT count(*) FROM Towns'
cur.execute(sql)
print(cur.fetchone()[0])

conn.commit()

sql = 'SELECT count(*) FROM Towns'
cur.execute(sql)
print(cur.fetchone()[0])

print('=' * 60)
