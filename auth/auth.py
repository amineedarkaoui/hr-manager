from DB.database import get_emails

def authenticate(email, password):
	if email in get_emails():
		if password == "password":
