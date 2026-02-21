import sqlite3

conn = sqlite3.connect('database.sqlite') # Opens connection between Python script and SQLite 
cursor = conn.cursor() # Cursor is a middleman between Python and database. conn.cursor() lets you to start running SQL statements.

# print("Opened database successfully")

# cursor.execute("DELETE FROM EMPLOYEE") # runs a single SQL command

# # Create table
# cursor.execute('''
# CREATE TABLE IF NOT EXISTS EMPLOYEE (
#     ID INT PRIMARY KEY NOT NULL,
#     NAME TEXT NOT NULL,
#     AGE INT NOT NULL
# );
# ''')

# # Insert records
# cursor.execute("INSERT INTO EMPLOYEE (ID, NAME, AGE) VALUES (1, 'Razi', 14)")
# cursor.execute("INSERT INTO EMPLOYEE (ID, NAME, AGE) VALUES (2, 'Jon', 19)")
# cursor.execute("INSERT INTO EMPLOYEE (ID, NAME, AGE) VALUES (3, 'Martha', 35)")

# conn.commit() # commit() saves the changes to the database.

# # To see result:
# cursor.execute('SELECT * FROM EMPLOYEE')
# rows = cursor.fetchall() #fetchall() retreves ALL ROWS from query. While fetchone() retries ONE ROW.
# for row in rows:
#     print(row)

# cursor.close() #close() closes the cursor and its optional
# conn.close()



# Create table
cursor.execute('''
CREATE TABLE IF NOT EXISTS STUDENT (
    ID INT PRIMARY KEY NOT NULL,
    NAME TEXT NOT NULL,
    GRADE INT NOT NULL
);
''')

# Insert records
cursor.execute("INSERT INTO STUDENT (ID, NAME, GRADE) VALUES (1, 'Razi', 3)")
cursor.execute("INSERT INTO STUDENT (ID, NAME, GRADE) VALUES (2, 'Jon', 3)")
cursor.execute("INSERT INTO STUDENT (ID, NAME, GRADE) VALUES (3, 'Martha', 6)")

conn.commit() # commit() saves the changes to the database.

# To see result:
cursor.execute('SELECT * FROM STUDENT')
rows = cursor.fetchall() #fetchall() retreves ALL ROWS from query. While fetchone() retries ONE ROW.
for row in rows:
    print(row)

cursor.close() #close() closes the cursor and its optional
conn.close()