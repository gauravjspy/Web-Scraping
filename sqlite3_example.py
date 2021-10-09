import sqlite3

conn = sqlite3.connect('dbtest.db')
c = conn.cursor()

#delete table
#c.execute('''DROP TABLE employee''')

#create a table
c.execute('''CREATE TABLE employee(emp_id INT, email TEXT, password TEXT, hash_value TEXT)''')

#data to insert
emp_id = 1
email = 'test@gmail.com'
password = '123'
hashvalue = 'hdoierklsdhoewas'

#insert and commit to database
c.execute('''INSERT INTO employee VALUES(?,?,?,?)''', (emp_id, email, password, hashvalue))
conn.commit()

#select all data from table and print
c.execute('''SELECT * FROM employee''')
results = c.fetchall()
print(results)

#close database connection
conn.close()
