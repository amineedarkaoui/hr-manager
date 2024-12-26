import sqlite3

conn = sqlite3.connect("database.db")
cursor = conn.cursor()

# Additional departments
new_departments = [
    ("Legal"),
    ("Sales"),
    ("Operations"),
    ("Customer Support")
]
cursor.executemany("INSERT INTO Department (department_name) VALUES (?)", [(d,) for d in new_departments])

# Additional employees
new_employees = [
    ("Karim", "Tahiri", 14000, "Full-Time", "Legal Advisor", "karim.tahiri@example.com", "legal123"),
    ("Hanae", "Fazazi", 12500, "Full-Time", "Sales Representative", "hanae.fazazi@example.com", "salespass"),
    ("Nadia", "Jamal", 16000, "Full-Time", "Operations Manager", "nadia.jamal@example.com", "operations321"),
    ("Mohamed", "El Idrissi", 11000, "Part-Time", "Customer Support Agent", "mohamed.idrissi@example.com", "support987"),
    ("Rachid", "Oulad Ali", 14500, "Full-Time", "Operations Analyst", "rachid.oulaidali@example.com", "ops456"),
    ("Leila", "Abouzeid", 13500, "Full-Time", "HR Specialist", "leila.abouzeid@example.com", "hr987"),
    ("Imane", "Maarouf", 17500, "Full-Time", "Marketing Manager", "imane.maarouf@example.com", "marketing123"),
    ("Yassine", "Belghazi", 10000, "Part-Time", "IT Support", "yassine.belghazi@example.com", "it456"),
]

cursor.executemany("""
    INSERT INTO Employee (first_name, last_name, salary, employment_type, job_title, email, password)
    VALUES (?, ?, ?, ?, ?, ?, ?)
""", new_employees)

# Employee to Department relationships
new_employee_department = [
    (6, "Legal"),
    (7, "Sales"),
    (8, "Operations"),
    (9, "Customer Support"),
    (10, "Operations"),
    (11, "HR"),
    (12, "Marketing"),
    (13, "IT"),
]

cursor.executemany("""
    INSERT INTO EmployeeDepartment (employee_id, department_name)
    VALUES (?, ?)
""", new_employee_department)

# Attendance records for the new employees
new_attendance = [
    (6, "2024-12-20", 8.0),
    (6, "2024-12-21", 7.0),
    (7, "2024-12-20", 8.5),
    (8, "2024-12-20", 9.0),
    (9, "2024-12-20", 6.0),
    (10, "2024-12-20", 8.0),
    (11, "2024-12-20", 7.5),
    (12, "2024-12-20", 8.0),
    (13, "2024-12-20", 4.0),
]

cursor.executemany("""
    INSERT INTO Attendance (employee_id, day, time_per_day)
    VALUES (?, ?, ?)
""", new_attendance)

# Additional departments
more_employees = [
    ("Ahmed", "Tazi", 12500, "Full-Time", "Marketing Specialist", "ahmed.tazi@example.com", "mark123"),
    ("Yasmine", "El Idrissi", 11000, "Part-Time", "Content Writer", "yasmine.elidrissi@example.com", "content456"),
    ("Karim", "Nouaim", 16000, "Full-Time", "HR Specialist", "karim.nouaim@example.com", "hrspec789"),
    ("Hajar", "Mokhtar", 13500, "Full-Time", "Customer Support Specialist", "hajar.mokhtar@example.com", "custsup123"),
    ("Mohammed", "El Ouafi", 14500, "Full-Time", "Legal Advisor", "mohammed.elouafi@example.com", "legal987"),
    ("Sara", "Maazouz", 15500, "Full-Time", "Project Manager", "sara.maazouz@example.com", "projman456"),
    ("Ilyas", "Bekkali", 17000, "Full-Time", "Accountant", "ilyas.bekkali@example.com", "account123"),
    ("Nadia", "Lamrani", 9500, "Part-Time", "Data Entry Clerk", "nadia.lamrani@example.com", "dataentry789"),
]

cursor.executemany("""
    INSERT INTO Employee (first_name, last_name, salary, employment_type, job_title, email, password)
    VALUES (?, ?, ?, ?, ?, ?, ?)
""", more_employees)

# Employee to Department relationships (using existing departments)
more_employee_department = [
    (22, "Marketing"),
    (23, "Public Relations"),
    (24, "Human Resources"),
    (25, "Customer Service"),
    (26, "Legal"),
    (27, "Operations"),
    (28, "Finance"),
    (29, "Data Management"),
]

cursor.executemany("""
    INSERT INTO EmployeeDepartment (employee_id, department_name)
    VALUES (?, ?)
""", more_employee_department)

# Attendance records for the additional employees
more_attendance = [
    (22, "2024-12-21", 8.0),
    (22, "2024-12-22", 7.5),
    (23, "2024-12-21", 6.0),
    (24, "2024-12-21", 8.0),
    (25, "2024-12-21", 7.5),
    (26, "2024-12-21", 9.0),
    (27, "2024-12-21", 8.0),
    (28, "2024-12-21", 7.0),
    (29, "2024-12-21", 4.5),
]

cursor.executemany("""
    INSERT INTO Attendance (employee_id, day, time_per_day)
    VALUES (?, ?, ?)
""", more_attendance)

#Additional employees
additional_employees = [
    ("Zineb", "Amrani", 12000, "Full-Time", "Logistics Coordinator", "zineb.amrani@example.com", "logistics123"),
    ("Omar", "Benjelloun", 15000, "Full-Time", "Procurement Officer", "omar.benjelloun@example.com", "procure321"),
    ("Fatima", "Azzouzi", 18000, "Full-Time", "Finance Analyst", "fatima.azzouzi@example.com", "finance789"),
    ("Rania", "Kabbaj", 9500, "Part-Time", "Training Assistant", "rania.kabbaj@example.com", "train456"),
    ("Mehdi", "Souissi", 20000, "Full-Time", "Quality Manager", "mehdi.souissi@example.com", "quality123"),
    ("Ayoub", "Berrada", 13000, "Full-Time", "IT Specialist", "ayoub.berrada@example.com", "itspec678"),
    ("Samira", "Hannouni", 14000, "Full-Time", "Public Relations Specialist", "samira.hannouni@example.com", "pr456"),
    ("Hicham", "Toumi", 17000, "Full-Time", "Business Analyst", "hicham.toumi@example.com", "bizana789"),
]

cursor.executemany("""
    INSERT INTO Employee (first_name, last_name, salary, employment_type, job_title, email, password)
    VALUES (?, ?, ?, ?, ?, ?, ?)
""", additional_employees)

additional_attendance = [
    (14, "2024-12-20", 8.0),
    (14, "2024-12-21", 7.5),
    (15, "2024-12-20", 9.0),
    (16, "2024-12-20", 8.0),
    (17, "2024-12-20", 5.5),
    (18, "2024-12-20", 8.5),
    (19, "2024-12-20", 7.0),
    (20, "2024-12-20", 8.0),
    (21, "2024-12-20", 8.5),
]

cursor.executemany("""
    INSERT INTO Attendance (employee_id, day, time_per_day)
    VALUES (?, ?, ?)
""", additional_attendance)


# Commit changes and close the connection
conn.commit()
conn.close()