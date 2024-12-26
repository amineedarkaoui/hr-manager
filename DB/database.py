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

def get_all_users():
	cur, con = connectDB()
	users = cur.execute("SELECT * FROM Employee").fetchall()
	con.close()
	return users

def store_feedback(userId, answer1, answer2, answer3, sentiment1, sentiment2, sentiment3):
	cur, con = connectDB()
	data = [
		(userId, answer1, sentiment1),
		(userId, answer2, sentiment2),
		(userId, answer3, sentiment3)
	]
	cur.executemany("INSERT INTO Feedback (employee_id, feedback_text, sentiment) VALUES (?, ?, ?)", data)
	con.commit()
	con.close()

def print_all_feedbacks():
	cur, con = connectDB()
	cur.execute("SELECT * FROM Feedback")
	feedbacks = cur.fetchall()
	con.close()
	for feedback in feedbacks:
		print(feedback)