"""
* @Author: Mohammad Fatha
* @Date: 2021-10-14 11:07
* @Last Modified by: Mohammad Fatha
* @Last Modified time: 2021-10-15 00:44 
* @Title: : Python program for Indexes in Mysql
"""
import mysql.connector 
import os
from dotenv import load_dotenv, main
from LoggerHandler import logger
load_dotenv()

class MysqlIndex:

    '''
        Description:
            This class to execute the MySql Index concept
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
            self.db_connection.execute("CREATE DATABASE Student_Index")
            self.db_connection.execute("USE Student_Index")
            self.db_connection.execute("CREATE TABLE student_table(Student_ID INT, Student_Name varchar(255),Percentage INT,Age INT, Gender char(1), City INT, Course INT, PRIMARY KEY(Student_ID))")
            insert_query = "INSERT INTO student_table (Student_ID,Student_Name,Percentage,Age,Gender,City,Course) VALUES (%s,%s,%s,%s,%s,%s,%s)"
            insert_values = [
                                (1,'Ram',45,22,'M',1,1),
                                (2,'Sarita',85,21,'F',2,2),
                                (3,'Salman',39,20,'M',1,1),
                                (4,'Juhi',47,20,'F',3,1),
                                (5,'Anil',74,19,'M',1,3),
                                (6,'John',65,21,'M',2,2),
                                (7,'Shahid',63,20,'M',1,3)
                            ]
            self.db_connection.executemany(insert_query,insert_values)
            self.db_connection.execute("SHOW DATABASES")
            for db in self.db_connection:
                print(db)
            logger.info("Databases are Successfully created")
        except Exception as e:
            logger.error("Exception Occured",e)

    def create_index_table_db(self):
        '''
        Description:
            This function is used to create indexes for the column in table
        '''
        try:
            self.db_connection.execute("SELECT * FROM student_table WHERE Percentage > 60")
            print("Student percentage before adding indexes")
            for students in self.db_connection:
                print(students)
            self.db_connection.execute("CREATE INDEX studpercent ON student_table(Percentage)")
            print("Create Indexs of the table")
            for students in self.db_connection:
                print(students)
            self.db_connection.execute("SELECT * FROM student_table WHERE Percentage > 60")
            print("Student oercentage before adding indexes")
            for students in self.db_connection:
                print(students)
            self.db_connection.execute("SHOW INDEX FROM student_table")
            print("Show Indexs of the table")
            for indexs in self.db_connection:
                print(indexs)
            logger.info("Indexes for the table's column successfully created")
        except Exception as e:
            logger.error("Exception Occured", e)

    def drop_indexs_in_table(self):
        '''
        Description:
            This function is used to Delte indexes for the column in table
        '''
        try:
            self.db_connection.execute("DROP INDEX studpercent on student_table ")
            print("Show Indexs of the table")
            self.db_connection.execute("SHOW INDEX FROM student_table")
            for indexs in self.db_connection:
                print(indexs)
            logger.info("Indexes of the tabled deleted")
        except Exception as e:
            logger.error("Exception Occured",e)



if __name__ == '__main__':

    indexes = MysqlIndex()
    indexes.create_Student_db()
    indexes.create_index_table_db()
    indexes.drop_indexs_in_table()