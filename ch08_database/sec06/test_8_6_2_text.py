# -*- coding: utf-8 -*-
import os
import shutil
import sqlite3 as sqlite

import config

os.chdir('/home/bk/tmp')

conn = sqlite.connect('xx_out3.sqlite')

conn.enable_load_extension(True)
conn.execute('SELECT load_extension("libspatialite.so.5")')
cur = conn.cursor()

cvs_text = '''Author,Book,Lang,Category,Price
"Alighieri, Dante",Divina commedia,Italian,Literature,"12,50"
"Hobbes, Thomas",The Leviathan,English,Philosophy,"18,75"
"Shakespeare, William",Julius Cesar,English,Literature,"8,25"
"Knut, Donald",The art of computer programming,English,Computing,"35,50"
Stendhal,Le rouge et le noir,French,Literature,"8,50"
"Gould, Stephen Jay",Wonderful life,English,Biology,"12,60"
"Diderot, Denis",Jacques le fataliste,French,Literature,"6,50"
"Mann, Heinrich",Der blaue Engel,German,Literature,"6,60"
"Caesar, Caius Julius",Commentarii de bello gallico,Latin,History,"15,00"
"Morris, Desmond",The naked ape,English,Biology,"8,75"
"Kerningham, Brian : Ritchie, Dennis",The C programming Language,English,Computing,"17,50"
"de Cervantes, Miguel",Don Quichote,Spanish,Literature,"14,20"
Voltaire,Trait茅 sur la tol茅rance,French,Philosophy,"12,00"
"Mann, Thomas",Der Zauberberg,German,Literature,"11,00"
"Darwin, Charles",Origin of the Species,English,Biology,"9,50"
"Gibson, Henry W.",The decline and fall of the Roman Empire,English,History,"18,50"
"Flaubert, Gustave",L'茅ducation sentimentale,Literature,French,"7,50"
"Thackeray, William M.",Vanity fair,English,Literature,"10,00"
"Zola, Emile",Germinal,French,Literature,"8,40"
"Dawkins, Richard",The selfish gene,English,Biology,"12,50"
"Dickens, Charles",Our mutual friend,English,Literature,"9,30"
"Marx, Karl",Grundrisse der Kritik der politischen OEkonomie,German,Philosophy",10,00"
"Manzoni, Alessandro",I promessi sposi,Italian,Literature,"15,00"'''

with open('xx_out.txt', 'w') as fo:
    fo.write(cvs_text)
#

sql = "CREATE VIRTUAL TABLE books USING VirtualText(xx_out.txt, utf8, 1, COMMA, DOUBLEQUOTE, ',');"
res = conn.execute(sql)
#
# sql2 = "SELECT * FROM books ORDER BY Lang, Author;"
# res3 = cur.execute(sql2)
#
# for rec in res3:
#     print(rec)
