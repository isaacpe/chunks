#!/usr/bin/python3
# -*- coding: utf_8 -*-
from chunkslib import *
#global kubu, ctable
#rv = ht_get_parms("upload")
#log(rv)
ht_header("upload_process")
form = cgi.FieldStorage()
filedata = form['upload']
name = random_string(10)
old_name = filedata.filename
ext = old_name.split(".")[-1]
log(old_name)
if filedata.file:
    with open("data/files/" + name + "." + ext, 'wb') as outfile:
        outfile.write(filedata.file.read())
