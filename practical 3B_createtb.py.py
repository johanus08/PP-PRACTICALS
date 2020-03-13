import mysql.connector as mysql
conn = mysql.connect(user="admin",password="scott",host='127.0.0.1')
c=conn.cursor()
c.execute("Use johanus")
c.execute("create table  students(s_id int(5),sname varchar(20),s_loc  varchar(20))")

conn.close()
