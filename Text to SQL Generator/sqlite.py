import sqlite3

# Connect to SQlite
connection=sqlite3.connect("students.db")

# create a cursor object to inset record, create table
cursor=connection.cursor()

cursor.execute("DROP TABLE IF EXISTS student;")

## create the table
table_info="""
CREATE TABLE student(
    name VARCHAR(25),
    class VARCHAR(25),
    section VARCHAR(25),
    marks INT
);
"""

cursor.execute(table_info)

cursor.execute("INSERT INTO student values('Elon Musk', 'Sceince', 'A', 60)")
cursor.execute("INSERT INTO student values('Trump', 'Politics', 'B', 75)")
cursor.execute("INSERT INTO student values('Modi', 'Politics', 'B', 80)")
cursor.execute("INSERT INTO student values('Rohit', 'Sceince', 'A', 100)")


print("******** inserted records are *********")
data=cursor.execute("SELECT * FROM student")

for row in data:
    print(row)

cursor.close()
connection.commit()
connection.close()
