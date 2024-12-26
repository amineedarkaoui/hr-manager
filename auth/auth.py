from DB.database import get_user

def authenticate(email, password):
	user = get_user(email)
	if user:
		if (user[7] == password):
			return True , user
		else:
			return ("Incorrect Password"), None
	else:
		return ("User not found"), None

