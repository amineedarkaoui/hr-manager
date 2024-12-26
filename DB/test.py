import database

def select_all_feedback():
    cur, con = database.connectDB()
    cur.execute("SELECT * FROM Employee")
    Employee = cur.fetchall()
    con.close()
    return Employee

# Example usage
Employee_records = select_all_feedback()

print("all feedbacks reocords : ")
for record in Employee_records:
    print(record)