import sqlite3

conn = sqlite3.connect('example.db')
print("Opened Database Succcessfully")

conn.execute("INSERT INTO EMPLOYEES VALUES (1,'FAITH KARIMI',23,345000.00)")
conn.execute("INSERT INTO EMPLOYEES VALUES (2,'BOB KURIA',32,150000.00)")
conn.execute("INSERT INTO EMPLOYEES VALUES (3,'JANE MUTHONI',27,165000.00)")
conn.execute("INSERT INTO EMPLOYEES VALUES (4,'MARY ANNE',38,160000.00)")
conn.execute("INSERT INTO EMPLOYEES VALUES (5,'PAUL KAMAU',29,145000.00)")

conn.commit()
print("Records Inserted Successfully")
conn.close()