
import pandas as pd
import pyodbc
class UsingAgencyModel: 
    def __init__(self, using_agency_code, using_agency_name): 
        self.using_agency_code = using_agency_code 
        self.using_agency_name = using_agency_name

class UsingAgency:
    def createTable(self):
        cursor = self.connection.cursor()
        cursor.execute(self.create_table_sql)
        self.connection.commit()

    create_table_sql = '''            CREATE TABLE UsingAgencies (
                using_agency_id int primary key IDENTITY NOT NULL,
                using_agency_code nvarchar(50),
                using_agency_name nvarchar(50)
                );
                '''
    table_name = 'UsingAgencies'
    insert_using_agency_query = "insert into UsingAgencies (using_agency_name, using_agency_code) values (?, ?)"
    get_using_agency_by_id = "select using_agency_id from UsingAgencies where using_agency_code=? and using_agency_name=?"

    
    
    def __init__(self, agency_code_column, agency_name_column, connection):
        self.agency_code_column = agency_code_column
        self.agency_name_column = agency_name_column
        self.connection = connection
        #self.createTable()

    def getUsingAgencyId(self, using_agency_code, using_agency_name):
        cursor = self.connection.cursor()
        cursor.execute(self.get_using_agency_by_id, (str(using_agency_code), using_agency_name))
        using_agency_id = cursor.fetchone()
        if using_agency_id is None:
            return 0
        return using_agency_id[0]

    def saveDatabase(self, using_agency_item):
        agency_val = (using_agency_item.using_agency_name, int(using_agency_item.using_agency_code))
        cursor = self.connection.cursor()
        cursor.execute(self.insert_using_agency_query, agency_val)
        self.connection.commit()

    def separateData(self):
        using_agency_list = []
        using_agency_names = self.agency_name_column.unique()
        using_agency_codes = self.agency_code_column.unique()
        for i in range(len(using_agency_names)):
            using_agency_list.append(UsingAgencyModel(using_agency_codes[i], using_agency_names[i]))


        for using_agency_item in using_agency_list:
            if(pd.isna(using_agency_item.using_agency_name)):
                using_agency_item.using_agency_name = "null"

            if(pd.isna(using_agency_item.using_agency_code)):
                using_agency_item.using_agency_code = 0
            self.saveDatabase(using_agency_item)