import sqlite3

conn = sqlite3.connect('example.db')
print("Opened Database Successfully")

conn.execute('''CREATE TABLE EMPLOYEES(
ID INT PRIMARY KEY NOT NULL, 
NAME TEXT NOT NULL,
AGE INT NOT NULL,
SALARY REAL NOT NULL
);''')

print("Table Created Successfully")
conn.close()