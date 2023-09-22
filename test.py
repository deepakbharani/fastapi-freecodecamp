import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="Apples#1994", 
    database="finaccdb",
    consume_results=True
)


mycursor = mydb.cursor()


sql = "DELETE FROM supplier_table WHERE s_name = 'AAA' "
mycursor.execute(sql)
mydb.commit()


### CREATE AND SHOW DATABASE
# mycursor.execute("CREATE DATABASE finaccdb")
# mycursor.execute("SHOW DATABASES")

# for db in mycursor:
#     print(db)

### CREATE AND SHOW TABLE
# mycursor.execute("CREATE TABLE supplier_table (s_name VARCHAR(255), s_address VARCHAR(255), s_email VARCHAR(225), s_vatno VARCHAR(255), s_bank_name VARCHAR(225), s_accno VARCHAR(225), s_bic VARCHAR(255))")

# mycursor.execute("SHOW TABLES")

# for tb in mycursor:
#     print(tb)

### POPULATE THE CREATED TABLE
# sql = "INSERT INTO supplier_table (s_name, s_address, s_email, s_vatno, s_bank_name, s_accno, s_bic) VALUES (%s, %s, %s, %s, %s, %s, %s)"
# suppliers = [   ("AAA", "Dietostrasse 25, 88046 Friedrichshafen", "aaa@gmail.com", "12345abcd", "Yes Bank", "123738927826hjasodh2", "hdhek292928172"),
#                 ("EAA", "Dietostrasse 25, 88046 Friedrichshafen", "eaa@gmail.com", "32345abcd", "Yes Bank", "123738927826hjasode2", "hdhek292928173"),
#                 ("FFA", "Dietostrasse 25, 88046 Friedrichshafen", "ffa@gmail.com", "34345abcd", "Yes Bank", "123738927826hjasofe2", "hdhek292928143")]

# mycursor.executemany(sql, suppliers)
# mydb.commit()

### GET DATA FROM TABLE
# mycursor.execute("SELECT s_name FROM supplier_table")
# myresult = mycursor.fetchone()

# for row in myresult:
#     print(row)

### GET DATA FROM TABLE USING WHERE 

# sql = "SELECT * FROM supplier_table WHERE s_name LIKE '%A'"
# mycursor.execute(sql)

# myresult = mycursor.fetchall()

# for res in myresult:
#     print(res)

### UPDATE DATA IN THE TABLE
# sql = "UPDATE supplier_table SET s_name = 'BAA' WHERE s_email = 'eaa@gmail.com' "
# mycursor.execute(sql)
# mydb.commit()

### ORDER DATA IN THE TABLE
# sql = "SELECT * FROM supplier_table ORDER BY s_name"
# or
# sql = "SELECT * FROM supplier_table ORDER BY s_name DESC"
# mycursor.execute(sql)
# mydb.commit()