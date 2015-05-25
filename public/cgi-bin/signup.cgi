#!/usr/bin/python

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

form = cgi.FieldStorage()
username=form['username'].value
password=form['password'].value
email   =form['email'].value

bodystring = ""
# check if username is not already present in the database
if (db.user_exists(username)):
	bodystring = "Your username is already in use! pick another one<br>"
else: # insert the user in the database
	db.add_user(username,password,email)
	bodystring = "Congratulations {:s}, you have succesfully registered".format(username)

print("Content-Type: text/html\n\n")
print("<html>")
print("<head>")
print("<title>This is the title</title>")
print("Your username was {:}<br>".format(username))
print("Your password was {:}<br>".format(password))
print(bodystring)
print("</head>")
print("</html>")

