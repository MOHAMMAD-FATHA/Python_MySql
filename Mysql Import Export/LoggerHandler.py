import logging

logger = logging

# Basic configuration and required format of the file
logger.basicConfig(filename="/home/fatha/Documents/MySql/Mysql Import Export/MysqlImportExport.log",
                    level=logging.INFO, format='%(asctime)s:%(funcName)s:%(levelname)s:%(message)s')

logger.basicConfig(filename="/home/fatha/Documents/MySql/Mysql Import Export/MysqImportExport.log",
                    level=logging.ERROR, format='%(asctime)s:%(funcName)s:%(levelname)s:%(lineo)d')