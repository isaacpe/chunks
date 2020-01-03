#!/usr/bin/python3

import os
from chunkslib import *
ht_header("cookie")
a = ht_get_cookie()
print(a)
user, gtime = a.split('//')
itime = float(gtime)
# print(user)
# print(itime)
ctime=time.time() 
print("difference={}".format(ctime-itime))
if ctime-itime > 600:
    user = ""
print(user)
