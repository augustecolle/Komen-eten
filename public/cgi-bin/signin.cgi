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
mod = imp.find_module("session_manager",["."])
session_manager = imp.load_module("session_manager",*mod)


import cgi,cgitb; cgitb.enable()
from user_database import UserDatabase
import Cookie,uuid

db = UserDatabase()

bodystring=""	


form = cgi.FieldStorage()
username=form['username'].value
password=form['password'].value

cookie = Cookie.SimpleCookie()

if (db.user_exists(username) and db.check_password(username,password) ):
	sessionM = session_manager.sessionManager()
	session_id = sessionM.new_session(username)
	cookie["username"]   = username
	cookie["session_id"] = session_id
	bodystring = "Welcome {:s}, you succesfully logged in ".format(username)		
	headstring = "<meta HTTP-EQUIV=\"REFRESH\" content=\"3; url=../index.html\">"
	print(cookie) # important that this comes before Content-Type:....
else:
	headstring = "<meta HTTP-EQUIV=\"REFRESH\" content=\"3; url=../index.html\">"
	bodystring = "Invalid username or password<br>\n"
	bodystring+= " user exists ? "+str(db.user_exists(username))+"<br>\n"
	bodystring+= " check passwd? "+str(db.check_password(username,password))+"<br><br>\n"

print("Content-type: text/html\n\n")
print("<html>")
print("<head>")
print(headstring)
print("<title>This is the title</title>")
print("Your username was {:}<br>".format(form['username'].value))
print("Your password was {:}<br>".format(form['password'].value))
print(bodystring)
import os
print("Path is {:s}".format(os.getcwd()))
print(form)
print("</head>")
print("</html>")

