from DB.database import get_user

def authenticate(email, password):
	if get_user(email):
		if (get_user(email)[7] == password):
			return True
		else:
			return ("Incorrect Password")
	else:
		return ("User not found")

