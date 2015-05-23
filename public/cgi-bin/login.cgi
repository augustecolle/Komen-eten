#!/usr/bin/python

import cgi,cgitb

cgitb.enable()

print("Content-Type: text/html\n\n")


form = cgi.FieldStorage()

print("<html>")
print("<head>")
print("<title>This is the title</title>")
print("Your username was {:}<br>".format(form['username'].value))
print("Your password was {:}<br>".format(form['password'].value))
print("</head>")
print("</html>")

