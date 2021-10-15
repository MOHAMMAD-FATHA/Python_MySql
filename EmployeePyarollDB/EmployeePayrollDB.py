"""
* @Author: Mohammad Fatha
* @Date: 2021-10-12 18:07
* @Last Modified by: Mohammad Fatha
* @Last Modified time: 2021-10-13 02:44 
* @Title: : Python program for employee payroll using MySql
"""

from LoggerHandler import logger
import mysql.connector
import os
from dotenv import load_dotenv
load_dotenv()

class EmployeePayroll:

    '''
        Description:
            This class consist of CRUD operations method for employee payroll database

    '''
    
    def __init__(self):
        
        self.db_conn = mysql.connector.connect(
            host = os.getenv("HOST"),
            user = os.getenv('USER1'),
            password = os.getenv('PASSWD'),
            auth_plugin = os.getenv('PLUGIN')
            )
        self.db_connection = self.db_conn.cursor()
    
   
    def create_employee_payroll_db(self):
        '''
            Description:
                This function is use to create the employee payroll database
        '''
        try:
            self.db_connection.execute("CREATE DATABASE employee_payroll_db")
            self.db_connection.execute("CREATE DATBASE emp_wage")
            self.db_connection.execute("SHOW DATABASES")
            for db in self.db_connection:
                print(db)
            logger.info("Query Successfully Executed")
        except Exception as e:
            logger.error(print("Exception Occure",e))

    
    def create_employee_payroll_table(self):
        '''
            Description:
                This function is use to create the employee payroll table in selected database
        '''
        try:
            self.db_connection.execute("USE employee_payroll_db")
            self.db_connection.execute("CREATE TABLE employee_payroll_table(Emp_ID INT, Emp_Name varchar(255), Designation varchar(255), Salary INT)")
            self.db_connection.execute("CREATE TABLE employee_wage_table(Emp_ID INT, Emp_Name varchar(255), Designation varchar(255), Salary INT)")
            insert_query = "INSERT INTO depart (id,empname,name,branch,employ,sal) VALUES (%s,%s,%s,%s,%s,%s)"
            insert_values = [
                                (2,'vithika','Admin depart','registration',15,40000),
                                (3,'Chintu','Humanities depart','langs',22,100000),
                                (4,'Riddi','Human resources','HR',12,20000),
                                (5,'Navi','Cultural','sports',45,50000)
                            ]
            self.db_cursor.executemany(insert_query,insert_values)
            self.db_connection.execute("SHOW TABLES")
            for table in self.db_connection:
                print(table)
            logger.info("Query Successfully Executed")
        except Exception as e:
            logger.error(print("Exception Occure",e))

    
    def insert_employee_data(self):
        '''
            Description:
                This function is use to add employee data in the table of created database
        '''
        try:
            self.db_connection.execute("USE employee_payroll_db")
            self.db_connection.execute("INSERT INTO employee_payroll_table VALUES (1, 'Mohammad FATHA', 'DATA ENGINEER', 30000)")
            self.db_connection.execute("INSERT INTO employee_payroll_table VALUES (2, 'AYUSH', 'DESIGN ENGINEER', 60000)")
            self.db_connection.execute("INSERT INTO employee_payroll_table VALUES (3, 'PRIYA', 'HR', 40000)")
            self.db_connection.execute("SELECT * FROM employee_payroll_table")
            for details in self.db_connection:
                print(details)
            
            logger.info("Query Successfully Executed")
        except Exception as e:
            logger.error(print("Exception Occure",e))
    
    
    def retrive_employee_data(self):
        '''
            Description:
                This function is retrive the data based on condition given
        '''
        try:
            self.db_connection.execute("USE employee_payroll_db")
            self.db_connection.execute("SELECT Salary FROM employee_payroll_table WHERE Emp_ID = 2")
            for salary in self.db_connection:
                print(salary)
            logger.info("Query Successfully Executed")
        except Exception as e:
            logger.error(print("Exception Occure",e))   
    
    
    def update_employee_data(self):
        '''
            Description:
                This function is update the records in a table
        '''
        try:
            self.db_connection.execute("USE employee_payroll_db")
            self.db_connection.execute("UPDATE employee_payroll_table SET Salary=50000  WHERE Emp_Name = 'MOHAMMAD FATHA'")
            self.db_connection.execute("SELECT * FROM employee_payroll_table")
            for details in self.db_connection:
                print(details)
            logger.info("Query Successfully Executed")
        except Exception as e:
            logger.error(print("Exception Occure",e)) 
    
    
    def del_employee_data(self):
        '''
            Description:
                This function is delete the records in a table
        '''
        try:
            self.db_connection.execute("USE employee_payroll_db")
            self.db_connection.execute("DELETE FROM employee_payroll_table  WHERE Emp_Name = 'PRIYA'")
            self.db_connection.execute("SELECT * FROM employee_payroll_table")
            for details in self.db_connection:
                print(details)
            self.db_connection.execute("DROP TABLE employee_wage_table")
            for table in self.db_connection:
                print(table)
            logger.info("Query Successfully Executed")
        except Exception as e:
            logger.error(print("Exception Occure",e))
    
    
    def drop_employee_db(self):
        '''
            Description:
                This function is delete the records in a table
        '''
        try:
            self.db_connection.execute("DROP DATABASE emp_wage")
            self.db_connection.execute("SHOW DATABASES")
            for db in self.db_connection:
                print(db)
            logger.info("Query Successfully Executed")
        except Exception as e:
            logger.error(print("Exception Occure",e))
    
    def __del__(self):
        self.db_conn.close()

   
if __name__ == '__main__':
    
    employee_payroll = EmployeePayroll()
    try:
        while(True):
            print(" 1.Create Databases\n2.Create tables\n3.Insert Data in Table:\n4.Retrive Data:\n5.Update data in table:\n6.Delete data from table:\n7.Drop the database:\n8.Exit:")
            option = int(input())
            if option == 1 :
                employee_payroll.create_employee_payroll_db()
            elif option == 2:
                employee_payroll.create_employee_payroll_table()
            elif option == 3:
                employee_payroll.insert_employee_data()
            elif option == 4:
                employee_payroll.retrive_employee_data()
            elif option == 5:
                employee_payroll.update_employee_data()
            elif option == 6:
                employee_payroll.del_employee_data()
            elif option == 7:
                employee_payroll.drop_employee_db()
            elif option == 8:
                break
    except ValueError:
        logger.error("Invalid Input")

