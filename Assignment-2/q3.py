import dbconn

connection=dbconn.get_connection()

def employee():
    #form a qery
    query = "select * from employees;"

    # create a cursor to execute query
    cursor = connection.cursor()

    # execute query using cursor
    cursor.execute(query)

    # get data from cursor
    records = cursor.fetchall()     #   returns list of tuples

    print(records)

    # close the cursor
    cursor.close()

    # close the connection
    connection.close()

def department(value):
    # temp=input("Enter department :")
    
    query = "select *from employees where dep=%s;"
    
    val=(value,)

    # create a cursor to execute query
    cursor = connection.cursor()

    # execute query using cursor
    cursor.execute(query,val)

    # get data from cursor
    records = cursor.fetchall()     #   returns list of tuples

    print(records)

    # close the cursor
    cursor.close()

    # close the connection
    connection.close()


def highest_salary():
        #form a qery
    query = "select salary from employees where salary=MAX;"

    # create a cursor to execute query
    cursor = connection.cursor()

    # execute query using cursor
    cursor.execute(query)

    # get data from cursor
    records = cursor.fetchall()     #   returns list of tuples

    print(records)

    # close the cursor
    cursor.close()

    # close the connection
    connection.close()

def Minimum_salary():
        #form a qery
    query = "select salary from employees where salary=MIN;"

    # create a cursor to execute query
    cursor = connection.cursor()

    # execute query using cursor
    cursor.execute(query)

    # get data from cursor
    records = cursor.fetchall()     #   returns list of tuples

    print(records)

    # close the cursor
    cursor.close()

    # close the connection
    connection.close()


employee()
dep=input("Enter dep:")
department(dep)
# highest_salary()
# Minimum_salary()


# select salary from employees;
