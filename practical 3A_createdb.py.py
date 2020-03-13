import mysql.connector as mysql
conn = mysql.connect(user="root",password="scott",host="127.0.0.1")
c=conn.cursor()

##c.execute("CREATE DATABASE johanus")
conn.close()
