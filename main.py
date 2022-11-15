
import pymysql.connections

#connect to the database

conn=pymysql.connect(host='localhost',
                        user='root',
                        password='admin',
                        database='demo2',
                        cursorclass=pymysql.cursors.DictCursor)
cursor = conn.cursor()

cursor.execute("DROP TABLE IF EXISTS EMPLOYEE")

#Creating table as per requirement
sql ='''CREATE TABLE EMPLOYEE(
   FIRST_NAME CHAR(20) NOT NULL,
   LAST_NAME CHAR(20),
   AGE INT,
   SEX CHAR(1),
   INCOME FLOAT
)'''
cursor.execute(sql)
conn.close()