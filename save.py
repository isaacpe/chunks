#!/usr/bin/python3
"""it is a process code to either update an existing
record or insert in DB if it does not exists"""
from chunkslib import *
global db_location
db = sqlite3.connect(db_location)
ht_header("saving")
parms = ht_get_parms(['ctn','index'])
index = parms[1]
ctn = parms[0]
if index != "0":
    try:
        db.execute('UPDATE pair SET content=? WHERE id=?', [ctn, index]) 
        db.commit()
        db.close()
    except:
        print("puto error en UPDATE")
else:
    try:
        index = count()
        db.execute('INSERT INTO pair VALUES(?,?)', [index, ctn])
        db.commit()        
        db.close()
    except:
        print("puto error en INSERT")
ht_redirect("/search.py")
