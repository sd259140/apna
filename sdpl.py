import mysql.connector
db=mysql.connector.connect(
    host="localhost",
    user="root",
    password="myroot")
    mycursor=db.cursor()
    sql= "select * from apna apna (id,asdte) values(%s,%s%s)"
    value="2007,pilib"
    mycursor.execute('se')
    mycursor.fetchall()
    db.commit()
