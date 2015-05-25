#!/usr/bin/env python

# this script uses passlib to hash the passwords
# to install it:
#
# pip install passlib
#
#
import imp # to find our user_database module
mod = imp.find_module("user_database",["."])
user_database = imp.load_module("user_database",*mod)

import cgi,cgitb; cgitb.enable()
from user_database import UserDatabase

db = UserDatabase()

bodystring=""	


form = cgi.FieldStorage()
username=form['username'].value
password=form['password'].value


if (db.user_exists(username) and db.check_password(username,password) ):
	bodystring = "Welcome {:s}, you succesfully logged in ".format(username)		
else:
	bodystring = "Invalid username/password<br>"
	bodystring+= " user exists ? "+str(db.user_exists(username))+"<br>"
	bodystring+= " check passwd? "+str(db.check_password(username,password))+"<br><br>"

print("Content-Type: text/html\n\n")
print("<html>")
print("<head>")
print("<title>This is the title</title>")
print("Your username was {:}<br>".format(form['username'].value))
print("Your password was {:}<br>".format(form['password'].value))
print(bodystring)
import os
print("Path is {:s}".format(os.getcwd()))
print(form)
print("</head>")
print("</html>")

