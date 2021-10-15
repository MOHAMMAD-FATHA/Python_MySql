"""
* @Author: Mohammad Fatha
* @Date: 2021-10-15 10:15
* @Last Modified by: Mohammad Fatha
* @Last Modified time: 2021-10-16 00:58
* @Title: : Python program for Views in Mysql
"""
import mysql.connector 
import os
from dotenv import load_dotenv, main
from LoggerHandler import logger
load_dotenv()

class MysqlView:

    '''
        Description:
            This class to execute the MySql View concept
    '''
    
    def __init__(self):
        
        self.db_conn = mysql.connector.connect(
            host = os.getenv("HOST"),
            user = os.getenv('USER1'),
            password = os.getenv('PASSWD'),
            auth_plugin = os.getenv('PLUGIN')
            )
        self.db_connection = self.db_conn.cursor()

    
    def create_Student_db(self):
        '''
        Description:
            This function is used to create indexes to the columns of the table
        '''
        try:
            self.db_connection.execute("CREATE DATABASE Student_View")
            self.db_connection.execute("SHOW DATABASES")
            for db in self.db_connection:
                print(db)
            self.db_connection.execute("USE Student_View")
            self.db_connection.execute("CREATE TABLE student_Details_table(S_ID INT, Names varchar(255),Address varchar(255))")
            self.db_connection.execute("CREATE TABLE student_Marks_table(ID INT, Name varchar(255),Marks INT, Age INT)")
            insert_query = "INSERT INTO student_Details_table (S_ID,Names,Address) VALUES (%s,%s,%s)"
            insert_values = [
                                (1,'Ram','Kolkata'),
                                (2,'Sarita','Dehli'),
                                (3,'Salman','Haryana'),
                                (4,'Juhi','Mumbai'),
                                (5,'Amit','Karnataka'),
                            ]
            self.db_connection.executemany(insert_query,insert_values)
            insert_query = "INSERT INTO student_Marks_table (ID,Name,Marks,Age) VALUES (%s,%s,%s,%s)"
            insert_values = [
                                (1,'Ram',90,19),
                                (2,'Sarita',50,20),
                                (3,'Salman',80,19),
                                (4,'Juhi',95,21),
                                (5,'Anil',85,18),
                            ]
            self.db_connection.executemany(insert_query,insert_values)
            logger.info("Databases successfully created")
        except Exception as e:
            logger.error("Exception occured",e)

    def create_view_table_db(self):
        '''
        Description:
            This function is used to create views for the tables
        '''
        try:
            self.db_connection.execute("CREATE VIEW DetailsView AS SELECT Names,Address FROM student_Details_table WHERE S_ID < 5")
            print("Student details whose ID is less then 5 uisng View")
            self.db_connection.execute("SELECT * FROM DetailsView")
            for students in self.db_connection:
                print(students)
            self.db_connection.execute("CREATE VIEW StudMarksAddress AS SELECT student_Details_table.Names, student_Details_table.Address, student_Marks_table.Marks FROM student_Details_table, student_Marks_table WHERE student_Details_table.Names = student_Marks_table.Name")
            print("Student details and marks from 2 different tables using view")
            self.db_connection.execute("SELECT * FROM StudMarksAddress")
            for students in self.db_connection:
                print(students)
            logger.info("View Created for the specified tables")
        except Exception as e:
            logger.error("Exception Occured ", e)

    def drop_view_of_table(self):
        '''
        Description:
            This function is used to delete  the view of the table
        '''
        try:
            print("Before deleting VIEW DetailsView")
            self.db_connection.execute("SHOW TABLES")
            for table in self.db_connection:
                print(table)
            print("After deleting VIEW DetailsView")
            self.db_connection.execute("DROP VIEW DetailsView")
            self.db_connection.execute("SHOW TABLES")
            for table in self.db_connection:
                print(table)
            logger.info("View Deleted for the specified tables")
        except Exception as e:
            logger.error("Exception occured",e)



if __name__ == '__main__':

    views = MysqlView()
    views.create_Student_db()
    views.create_view_table_db()
    views.drop_view_of_table()