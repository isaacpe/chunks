#!/usr/bin/python3

from chunkslib import *
global kubu
ht_header("list")
rv = ht_get_parms(["ctn"])
ctn = rv[0]
log("list - search string: "+ctn)
argv = ctn.split()
log("list - len argv"+str(len(argv)))
c=""
for i in range(0,len(argv)):
    c=c+"content like '%"+argv[i]+"%'"
    if i < len(argv) -1:
        c=c+" and "
if len(argv) == 0:
    c="select id, content from pair;"
else:
    c="select id, content from pair where ("+c+");"
log("sql = " + c)
data = db_exe(c)
ht_button("/search.py", "main")
print("<pre>")
print("TOTAL Matches: "+str(len(data))+"\n")
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
