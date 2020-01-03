#!/usr/bin/python3
"""this is the main page with options for search
and create new records"""

from chunkslib import *

log("in search beggining")
user = user_logged()
log(("user=",user))
if user == "":
    log("in user blank")
    ht_header("search") #needed for the redirect
    log("after header")
    ht_redirect("/login.py")
else:
    ht_set_cookie(user) 

ht_header("search")
ht_form_2b("/list.py", "search", "lucky")
ht_form("/new.py", "from template")
ht_button("/new.py", "new blank")
ht_form("/last.py", "last number")
