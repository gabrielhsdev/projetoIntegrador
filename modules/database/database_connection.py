from getpass import getpass
from mysql.connector import connect, Error

class dbPDO:

    def __init__(self):
        #connection complete
        try:
            with connect(
                host="localhost",
                user='root',
                password='admin',
            ) as connection:
                self.createInitializator()
                self.insertInitializator()

        except Error as e:
            print('Erro na conexão com o banco de dados')
            print(e)
            raise SystemExit
    
    #function used to set up envoirment database and table
    def createInitializator(self):
        queryDatabase = "CREATE DATABASE IF NOT EXISTS projeto_integrador_1"
        queryTable = "CREATE TABLE IF NOT EXISTS air_information ( id INT AUTO_INCREMENT PRIMARY KEY, timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP, MP10 FLOAT, MP2_5 FLOAT, O3 FLOAT, CO FLOAT, NO2 FLOAT, SO2 FLOAT );"
        self.query(queryDatabase, createDatabase=True)
        self.query(queryTable)
    
    #function used to insert initial values into table if any before
    def insertInitializator(self):
        count = self.query("select count(*) from air_information", True)
        if count[0][0] == 0:
            self.query("INSERT INTO air_information (timestamp, MP10, MP2_5, O3, CO, NO2, SO2) VALUES (NOW(), 12.1, 18.7,  4, 13,  3, 17);")
            self.query("INSERT INTO air_information (timestamp, MP10, MP2_5, O3, CO, NO2, SO2) VALUES (NOW(),   52,   17, 11,  3, 33,  7);")
            self.query("INSERT INTO air_information (timestamp, MP10, MP2_5, O3, CO, NO2, SO2) VALUES (NOW(),    1,  8.7,  8, 25, 15,  9);")
            self.query("INSERT INTO air_information (timestamp, MP10, MP2_5, O3, CO, NO2, SO2) VALUES (NOW(),   33,  1.7, 18, 16,  6, 18);")

    def query(self, query, fetchall=False, createDatabase = False):
        try:
            with connect(
                host="localhost",
                user='root',
                password='admin',
            ) as connection:
                try:
                    cursor = connection.cursor()
                    if createDatabase:
                        cursor.execute(query)
                        return cursor.rowcount
                    
                    cursor.execute("USE projeto_integrador_1")
                    cursor.execute(query)

                    if fetchall:
                        return cursor.fetchall()
                    else:
                        connection.commit()
                        return cursor.rowcount
                except Error as e:
                    print('Erro na query')
                    print(e)
                    raise SystemExit
        except Error as e:
            print('Erro na conexão com o banco de dados')
            print(e)
            raise SystemExit