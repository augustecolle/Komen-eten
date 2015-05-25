
import tinydb
from passlib.hash import pbkdf2_sha256


class UserDatabase:
	PRIVATE_DIR  =  "../private" #private dir relative to this script
	USER_DB      =  PRIVATE_DIR+"/users.json"

	# settings for the password encryption method pbkdf2_sha256
	HASH_ROUNDS    =  20000
	HASH_SALT_SIZE =  16
	
	def __init__(self):
		self.db = tinydb.TinyDB(self.USER_DB)
	
	def user_exists(self,username):
		return self.db.contains(tinydb.where('username')==username)
	
	def add_user(self,username,password,email):
		hash = pbkdf2_sha256.encrypt(password,rounds=self.HASH_ROUNDS,salt_size=self.HASH_SALT_SIZE)
		user = {'username':username,'password':hash,'email':email}
		self.db.insert(user)
	
	# return True if password is correct, False if not
	def check_password(self,username,password):
		hash = pbkdf2_sha256.encrypt(password,rounds=self.HASH_ROUNDS,salt_size=self.HASH_SALT_SIZE)
		return(pbkdf2_sha256.verify(password,self.db.get(tinydb.where('username')==username)['password']))
		
