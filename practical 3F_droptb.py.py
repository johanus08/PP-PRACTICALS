import mysql.connector as mysql
conn = mysql.connect(user="root",password="scott",host='127.0.0.1')
c=conn.cursor()
c.execute("use johanus")
c.execute("Drop table students")
c.execute("show tables from johanus")
print(c.fetchall())
conn.close()
