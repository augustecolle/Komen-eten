
import tinydb,uuid
import Cookie,os

class sessionManager(object):
	""" Class to manage sessions.
	This deals with reading and validating entries
	in the session database
	"""
	def __init__(self):
		self.db = tinydb.TinyDB("../private/sessions.json")
	def session_auth(self,username,session_id):
		return (self.session_exists(username) and self.session_id(username)==session_id)
	def session_exists(self,username):
		return self.db.contains(tinydb.where('username')==username)
	def session_id(self,username):
		return self.db.get(tinydb.where('username')==username)['session_id']
	def new_session(self,username):
		session_id = uuid.uuid4().hex
		self.register_session(username,session_id)
		return session_id
	def register_session(self,username,session_id):
		if self.session_exists(username):
			self.db.update({'session_id':session_id},tinydb.where('username')==username)
		else:
			self.db.insert({'username':username,'session_id':session_id})
	

# for now has a log file "flog", can be removed
class sessionAuth(object):
    """Wrapper class to make authenticated functions

    wrap your function that needs authentication like this

    @sessionAuth
    def yourfunction(*args):
    	...
    """
    def __init__(self,f):
	self.sessionM = sessionManager()
	self.f  = f
	
    def __call__(self,*args):
	flog = open("sessionAuth.log","a")
	flog.write("sessionAuth activated: ")
        try:
            cookie     = Cookie.SimpleCookie(os.environ["HTTP_COOKIE"])
	    username   = cookie["username"].value
            session_id = cookie["session_id"].value
	    flog.write("cookie was found:\n{:s}\n\n".format(cookie))
        except (Cookie.CookieError, KeyError): # no cookie could be read, do not allow calling of function
	    flog.write("cookie or key error!")
            return self.authentication_fail()
        
        #def authenticate_session(*args):
        if self.sessionM.session_auth(username,session_id): # authentication OK, proceed with calling 
	     flog.write("[SUCCES] authenticated!\n\n"); flog.close()
             return self.f(*args)
        else: # user is not in session database, return auth_fail
	     flog.write("[WARNING] session manager did not validate cookie\n")
	     flog.write("   > user {:s} in database? {:}\n".format(username,self.sessionM.session_exists(username)))
	     if self.sessionM.session_exists(username):
		     flog.write("   > session id is {:}".format(self.sessionM.session_id(username)))
	     flog.close()
             return self.authentication_fail()
        #return authenticate_session

    def authentication_fail(self):
    	print("Content-Type: text/html\n\n")
	print("<html><head><meta HTTP-EQUIV=\"REFRESH\" content=\"0; url=../login.html\"><body></body></html>")
        return None 


