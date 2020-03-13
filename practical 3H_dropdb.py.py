import mysql.connector as mysql
conn = mysql.connect(user="root",password="scott",host='127.0.0.1')
c=conn.cursor()
c.execute("use johanus")
c.execute("Drop database johanus")
c.execute("SHOW DATABASES")
print(c.fetchall())
conn.close()
