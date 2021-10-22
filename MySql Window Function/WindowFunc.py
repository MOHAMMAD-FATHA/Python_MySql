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

class MysqlWindows:

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
        
    
    def window_function_in_mysql(self):
        self.db_connection.execute("USE employee_payroll_db")
        self.db_connection.execute("""SELECT Name,Age,Department,Salary, 
                                    AVG(Salary) 
                                    OVER (PARTITION BY Department ORDER BY Age) 
                                    AS Avg_sal 
                                    FROM sale_table""")
        for procedures in self.db_connection:
            print(procedures)
    
    def rank_window_function_in_mysql(self):
        self.db_connection.execute("USE employee_payroll_db")
        self.db_connection.execute(""" SELECT 
                                    ROW_NUMBER() OVER (PARTITION BY Department ORDER BY Salary DESC) 
                                    AS emp_row_no, Name,  Department, Salary,
                                    RANK() OVER(PARTITION BY Department 
                                    ORDER BY Salary DESC) AS emp_rank,
                                    DENSE_RANK() OVER(PARTITION BY Department 
                                    ORDER BY Salary DESC) 
                                    AS emp_dense_rank
                                    FROM sale_table """)
        for procedures in self.db_connection:
            print(procedures)

if __name__ == '__main__':

    wnidows = MysqlWindows()
    wnidows.window_function_in_mysql()
    wnidows.rank_window_function_in_mysql()
   