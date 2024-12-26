import database

def select_all_feedback():
    cur, con = database.connectDB()
    cur.execute("SELECT * FROM Employee")
    Employee = cur.fetchall()
    con.close()
    return Employee

def show_tables():
    cur, con = database.connectDB()
    cur.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cur.fetchall()
    con.close()
    return [table[0] for table in tables]

#exemple usage : 
tables = show_tables()
print("tables in the databese : ",tables)


Employee_records = select_all_feedback()

print("all feedbacks reocords : ")
for record in Employee_records:
    print(record)