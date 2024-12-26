import sqlite3


def connectDB():
	con = sqlite3.connect("database.db")
	cur = con.cursor()
	return cur, con

def get_emails():
	cur, con = connectDB()
	cur.execute("SELECT email FROM Employee")
	emails = cur.fetchall()
	con.close()
	return [email[0] for email in emails]


