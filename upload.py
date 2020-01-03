#!/usr/bin/python3
# -*- coding: utf_8 -*-
from chunkslib import *
global kubu, ctable
ht_set_cookie("111111111111")
ht_header("upload")
rv = ht_get_parms(["index"])
index = str(rv[0])
ht_upload("./upload_process.py", "upload")
