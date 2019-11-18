#!/usr/bin/python3

import datetime
import os
def do_magic():
    now = datetime.datetime.now()
    return "Hello! {0}".format(now)

# WSGI "wiskey" standart for python
# sudo apt-get install uwsgi-plugin-python3 
# uwsgi  --plugin python3 --http-socket :9090 --wsgi-file app.py
def application(env, start_response):
    start_response('200 OK', [('Content-type:','text-html')])
    return [do_magic().encode()]

if __name__=="__main__":
    if 'REQUEST_URI' in os.environ:
      print("Content-type: text/html\n\n")
    print(do_magic())
 
