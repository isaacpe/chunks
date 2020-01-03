#!/usr/bin/python3

from chunkslib import *
global kubu
ht_header("new")
rv = ht_get_parms(["ctn"])
# can be coming from new(blank) or from_template if ctn is blank-non
a = ""
if rv[0] is not None:
    ctn = rv[0]
    log("ctn: "+ctn)
    a = file2var(kubu + "/templates/" + ctn)
ht_form_textarea("/save.py?index={}".format("0"), "save", a)

