#!/usr/bin/python3

from chunkslib import *
global kubu
ht_header("last")
rv = ht_get_parms(["ctn"])
ctn = rv[0]
l = last_id()
fr = int(l) - int(ctn)
log("last: ctn: "+str(ctn))
log("last: fr: "+str(fr))
c="select id, content from pair where id > '{}';".format(fr)
data = db_exe(c)
ht_button("/search.py", "main")
print("<pre>")
for row in data:
    index = str(row[0])
    print("""<a href="/edit.py?index={}">[{}]--></a>""".format(index,index))
    ln=row[1].split("\n")
    ln=ln[:-1]
    for i  in range(0,4):
        try:
            print(ln[i].translate(ctable))
        except:
            break
print("<pre>")
