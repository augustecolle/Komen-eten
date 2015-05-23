#!/usr/bin/python

import cgi,cgitb

cgitb.enable()

print("Content-Type: text/html\n\n")


form = cgi.FieldStorage()

