"""
* @Author: Mohammad Fatha
* @Date: 2021-10-14 11:07
* @Last Modified by: Mohammad Fatha
* @Last Modified time: 2021-10-15 00:44 
* @Title: : Python program for Import and Export in Mysql 
"""
import mysql.connector 
import os
from dotenv import load_dotenv
from LoggerHandler import logger
load_dotenv()

class MysqlImportExport:

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

    
    def export_database(self):
        '''
        Description:
            This function is used to export the database to file or dump DB to a file
        '''
        try:
            os.system("mysqldump -h 127.0.0.1 -u root -p  employee_payroll_db > emp_view_file.sql")
            print(os.system("head -n 5 emp_view_file.sql"))
            logger.info("Databases Exported to file")
        except Exception as e:
            logger.error("Exception Occured",e)

    def import_to_database(self):
        '''
        Description:
            This function is used to export the database to file or dump DB to a file
        '''
        try:
            self.db_connection.execute("CREATE DATABASE Emp_file_db")
            os.system("mysql -u username -p Emp_file_db < emp_view_file.sql")
            self.db_connection.execute("SHOW DATABASES")
            for db in self.db_connection:
                print(db)
            logger.info("Databases Exported to file")
        except Exception as e:
            logger.error("Exception Occured",e)



if __name__ == '__main__':
    importexport = MysqlImportExport()
    importexport.export_database
    importexport.import_to_database
    