#!/usr/bin/env python

# this script uses passlib to hash the passwords
# to install it:
#
# pip install passlib
#
#
import cgi,cgitb
from passlib.hash import pbkdf2_sha256
import json,os
cgitb.enable()

PRIVATE_DIR="../../private" #private dir relative to this script
PRIVATE_USER_FILE=PRIVATE_DIR+"/users.txt"
bodystring=""
try:
	userfile = open(PRIVATE_USER_FILE,"r")
	users=json.load(userfile)
except IOError:
	print("Error, no user database found, cannot check credentials")
	bodystring = "Error, no user database found, cannot check credentials"
	
print("Content-Type: text/html\n\n")


form = cgi.FieldStorage()

print("<html>")
print("<head>")
print("<title>This is the title</title>")
print("Your username was {:}<br>".format(form['username'].value))
print("Your password was {:}<br>".format(form['password'].value))
print(bodystring)
print(form)
print("</head>")
print("</html>")

