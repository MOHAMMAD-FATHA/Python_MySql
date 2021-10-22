"""
* @Author: Mohammad Fatha
* @Date: 2021-10-14 11:07
* @Last Modified by: Mohammad Fatha
* @Last Modified time: 2021-10-15 00:44 
* @Title: : Python program for Indexes in Mysql
"""
import mysql.connector 
import os
from dotenv import load_dotenv
# from LoggerHandler import logger
load_dotenv()

class MysqlProcedure:

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
        
    
    def create_procedure_for_table(self):
        self.db_connection.execute("USE employee_payroll_db")
        self.db_connection.execute("""CREATE PROCEDURE disp_emp()
                                      BEGIN
                                      SELECT * FROM employee_payroll_table;
                                      END""")
        self.db_connection.execute("EXEC disp_emp")
        for procedures in self.db_connection:
            print(procedures)

    def drop_procedures(self):
        self.db_connection.execute("USE employee_payroll_db")
        # List all the procedures present
        self.db_connection.execute("SHOW PROCEDURE STATUS  WHERE Db = DATABASE() AND Type = 'PROCEDURE'")
        self.db_connection.execute("DROP PROCEDURE IF EXISTS disp_emp")
        
if __name__ == '__main__':

    procedures = MysqlProcedure()
    procedures.create_procedure_for_table()
    procedures.drop_procedures()