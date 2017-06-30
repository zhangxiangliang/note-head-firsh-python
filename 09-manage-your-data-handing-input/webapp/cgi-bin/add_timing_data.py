#! /usr/local/bin/python3

import cgi
import os
import time
import sys
import yate

print(yate.start_response('text/plain'))
addr = os.environ['REMOTE_ADDR']
host = os.environ['REMOTE_HOST']
method = os.environ['REQUEST_METHOD']
cur_time = time.asctime()
print('--------Add-Timing-Data-Start--------', file=sys.stderr)
print('host: ' + host, file=sys.stderr)
print('addr: ' + addr, file=sys.stderr)
print('cur_time: ' + cur_time, file=sys.stderr)
print('method: ' + method, end=' ', file=sys.stderr)

form = cgi.FieldStorage()
for each_form_item in form.keys():
    print(each_form_item + '->' + form[each_form_item].value, file=sys.stderr)

print('--------Add-Timing-Data-End--------', file=sys.stderr)
print(file=sys.stderr)
print('Ok.')
