#!/usr/bin/python3
# -*- coding: utf_8 -*-
from chunkslib import *
global kubu, ctable
ht_header("edit")
rv = ht_get_parms(["index"])
index = str(rv[0])
ht_button("/search.py", "main")
data = db_exe("select content from pair where id='"+index+"';")
cco = data[0][0]
cco = cco.replace("\r\n", "\n")
cco = cco.translate(ctable)
ht_form_textarea("/save.py?index={}".format(index), "save", cco)
ht_spaces(2)
ht_button("/delete.py?index='{}'".format(index), "delete")
