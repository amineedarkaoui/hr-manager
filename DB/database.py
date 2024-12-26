import sqlite3

def connectDB():
	con = sqlite3.connect("database.db")
	cur = con.cursor()
	return cur, con

def get_user(email):
	cur, con = connectDB()
	user = cur.execute("SELECT * FROM Employee where email = ?", (email,)).fetchone()
	con.close()
	return user

