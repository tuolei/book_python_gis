

import sqlite3
conn = sqlite3.connect(":memory:")
conn.enable_load_extension(True)



import sqlite3
conn = sqlite3.connect(":memory:")
conn.enable_load_extension(True)
conn.execute('SELECT load_extension("libspatialite.so.5")')
curs = conn.cursor()

