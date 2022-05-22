import pyodbc
 
# Creating connection object
class Database:
    def connect(self):
        return pyodbc.connect('Driver={ODBC Driver 17 for SQL Server};'
                    'Server=RAST-MOBILE;'
                    'Database=frpp_public;'
                    'Trusted_Connection=yes;'
                   )
    
    def createTable(self, sql):
        cursor = self.connect().cursor()
        cursor.execute(sql)
        self.connect().commit()

    def insertData(self, sql, data):
        cursor = self.connect().cursor()
        cursor.execute(sql, data)
        self.connect().commit()

    def selectData(self, sql, data):
        cursor = self.connect().cursor()
        cursor.execute(sql,data)
        return cursor.fetchall()
    
    def closeConnection(self):
        self.connect().close()
