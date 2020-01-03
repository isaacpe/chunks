#!/usr/bin/python3
# -*- coding: utf_8 -*-
from chunkslib import *
global kubu, ctable
ht_header("login")
ht_form_start("/login_process.py")
ht_text('user','user')
ht_text('password', 'password')
ht_button_simple('enter')
ht_form_end() 
