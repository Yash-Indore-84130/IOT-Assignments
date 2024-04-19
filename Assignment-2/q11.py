import dbconn
# create a query
empid = int(input("Enter empid : "))
name = input("Enter name : ")
dep = input("Enter dep : ")
email = input("Enter email :")
salary = input("Enter salary : ")
doj=input("Enter Doj : ")

query = f"insert into employees values({empid}, '{name}', '{dep}', '{email}', '{salary}' ,'{doj}');"

connection=dbconn.get_connection()
# create a cursor to execute the query
cursor = connection.cursor()

# execute query using cursor
cursor.execute(query)

# after execution of query commit your changes
connection.commit()

# close the cursor
cursor.close()

#close the connection with mysql server 
connection.close()

