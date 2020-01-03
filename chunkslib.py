#!/usr/bin/python3
"""libreria para la aplicacion de chunks
tiene los temas de ht_ que son web interface
and the db for the access to sqlite"""
import sqlite3
import os
import random
import string
import cgi
import cgitb
import html.entities
import time

db_location = '/mnt/c/Users/isaac/ownCloud/mybin/kubu/data/my-data.db'
kubu ='/var/www/html'
logfile ='/var/log/chunks.log'
ctable = {k: '&{};'.format(v) for k, v in html.entities.codepoint2name.items()}
log_timeout = 1200 #in seconds 20 mins is 1200 secs

def count():
    global kubu
    db = sqlite3.connect(db_location)
    cur = db.cursor()
    sele="select value from keys where key='counter';"
    cur.execute(sele)
    data = cur.fetchall()
    cou=int(data[0][0])
    cou = cou + 1
    sele="update  keys set value="+str(cou)+" where key='counter';"
    cur.execute(sele)
    db.commit()
    db.close()
    return(cou)

def random_string(stringLength=10):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(stringLength))

def last_id():
    db = sqlite3.connect(db_location)
    sele = "SELECT id from pair order by id DESC limit 1;"
    cur = db.cursor()
    cur.execute(sele)
    data = cur.fetchall()
    cou=int(data[0][0])
    return cou

def ht_header(label):
    cgitb.enable()
    print ("Content-type: text/html\n\n")
    print ("""<meta charset="UTF-8">""")
    print("""<head>
            <link rel="stylesheet" href="chunks.css">
            </head>""")
    print ("ChUNKs - {}<br><br>".format(label))

def ht_upload(link, label):
    ft = """<form action="{}" method="POST" enctype="multipart/form-data">
        <input type="file" name="{}" id="{}">
        <input type="submit" value="upload">
        </form>"""
    print(ft.format(link, label, label))
    return

def ht_set_cookie(val):
    start = str(time.time())
    log("Set-Cookie: chunks={}//{}".format(val, start))
    print("Set-Cookie: chunks={}//{}".format(val, start))
    return

def ht_get_cookie():
    if "HTTP_COOKIE" in os.environ:
        cook = os.environ["HTTP_COOKIE"]
        log(cook)
        a = {}
        for i in cook.split("; "):
            ab=i.split("=")
            a[ab[0]]=ab[1]
        if 'chunks' in a.keys():
            return a['chunks']
    else:
        return '' 

def ht_get_parms(parm_names):
    arguments = cgi.FieldStorage()
    rv = []
    for p in parm_names:
        rv.append(arguments.getvalue(p))
    return rv


def db_exe(sql):
    db = sqlite3.connect(db_location)
    cur = db.cursor()
    cur.execute(sql)
    data = cur.fetchall()
    db.commit()
    db.close()
    return data

def file2var(fi):
    with open(fi, 'r') as fil:
        con = fil.read()
    return con

def log(rec):
    with open(logfile, 'a') as fil:
        print(rec, file=fil)
    fil.close()

def ht_textarea(ctn):
    print("""<textarea spellcheck="false" rows="20" cols="100">""" \
            + ctn + """</textarea>""")

def ht_translate(ctn):
    return ctn.translate(ctable)

def ht_redirect(url):
    print("<meta http-equiv='refresh' content='0;url={}' />".format(url))

def ht_form(link, button):
    print ("""<form action="{}" class="form-style-1" method="post">
        <input type="text" size="35" name="ctn"><br>
        <input type="submit" value="{}">
        </form>
        """.format(link, button))
 
def ht_form_2b(link, button1, button2):
    print("""<form action="{}" class="form-style-1" method="post">
        <input type="text" size="35" name="ctn"><br>
        <input type="submit" value="{}">""".format(link, button1))
    ht_spaces(18)
    print("""<input type="submit" value="{}"></form>""".format(button2))

def ht_form_textarea(link, button, ctn):
    print ("""<form action="{}" method="post">
        <textarea name="ctn" spellcheck="false" rows="20" cols="100">{}</textarea>
        <br>
        <input type="submit" value="{}">
        </form>
        """.format(link, ctn, button))

def ht_form_start(link):
    print("""<form action="{}" method="post">""".format(link))
    return

def ht_form_end():
    print("""</form>""")
    return

def ht_text(name, label):
    print("""<br>{}<br><input type="text" size="35" name="{}">""".format(label,name))
    return

def ht_button_simple(label):
    print("""<input type="submit" value="{}">""".format(label))
    return

def ht_button(link, button):
    print ("""<form action="{}" method="post">
        <input type="submit" value="{}">
        </form>
        """.format(link, button))

def ht_lines(n):
    for i in range(n):
        print("<br>")

def ht_spaces(n):
    for i in range(n):
        print("&nbsp;")

def user_logged():
    log("in user_logged")
    a = ht_get_cookie()
    log(("a=",a))
    user, gtime = a.split('//')
    itime = float(gtime)
    ctime=time.time() 
    if ctime-itime > log_timeout:
        user = ""
    log(("user=", user))
    return user

