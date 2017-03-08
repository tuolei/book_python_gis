# -*- coding: utf-8 -*-

import sqlite3
conn = sqlite3.connect(":memory:")
conn.enable_load_extension(True)



import sqlite3
conn = sqlite3.connect(":memory:")
conn.enable_load_extension(True)
# conn.execute('SELECT load_extension("libspatialite.so.5")')
conn.execute('SELECT load_extension("mod_spatialite.so.7")')
curs = conn.cursor()

