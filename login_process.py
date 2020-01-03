#!/usr/bin/python3
# -*- coding: utf_8 -*-
from chunkslib import *

user, password = ht_get_parms(["user", "password"])

if user == "isaac" and password == "trubia4":
    ht_set_cookie(user)
else:
    user = ""
ht_header("login_process")
print(user, password)
ht_redirect("/search.py")



