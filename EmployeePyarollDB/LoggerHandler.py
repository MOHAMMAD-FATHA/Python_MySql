import logging

logger = logging

# Basic configuration and required format of the file
logger.basicConfig(filename="/home/fatha/Documents/MySql/EmployeePyarollDB/EmployeePayrollDB.log",
                    level=logging.INFO, format='%(asctime)s:%(funcName)s:%(levelname)s:%(message)s')

logger.basicConfig(filename="/home/fatha/Documents/MySql/EmployeePyarollDB/EmployeePayrollDB.log",
                    level=logging.ERROR, format='%(asctime)s:%(funcName)s:%(levelname)s:%(lineo)d')