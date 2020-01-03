#!/usr/bin/python3

from chunkslib import *
global db_location
db = sqlite3.connect(db_location)
ht_header("deleting")
parms = ht_get_parms(['index'])
index = parms[0]
c="delete from pair where id="+index+";"
db_exe(c)
ht_redirect("/search.py")
