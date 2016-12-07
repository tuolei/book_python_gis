# -*- coding: utf-8 -*-
import os
import shutil
import sqlite3 as sqlite

import config

os.chdir(config.gisws)
shutil.copy("test-2.3.sqlite", 'xx_new_db.sqlite')

conn = sqlite.connect('xx_new_db.sqlite')

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
