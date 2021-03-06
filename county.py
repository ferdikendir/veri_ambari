import pandas as pd
import pyodbc
class CountyModel:
    def __init__(self, county_name, county_code):
        self.county_name = county_name
        self.county_code = county_code


class County:
    def createTable(self):
        cursor = self.connection.cursor()
        cursor.execute(self.create_table_sql)
        self.connection.commit()

    create_table_sql = '''            CREATE TABLE Counties (
                county_id int primary key IDENTITY NOT NULL,
                county_name nvarchar(50),
                county_code nvarchar(50)
                );
                '''
    table_name = 'Counties'
    insert_county_query = "insert into Counties (county_name, county_code) values (?, ?)"
    get_county_by_id = "select county_id from Counties where county_name=? and county_code=?"

    def __init__(self, county_code_column, county_name_column, connection):
        self.county_code_column = county_code_column
        self.county_name_column = county_name_column
        self.connection = connection
        #self.createTable()

    def getCountyId(self, county_name, county_code):
        cursor = self.connection.cursor()
        cursor.execute(self.get_county_by_id, (str(county_name), str(county_code)))
        row = cursor.fetchone()
        if row is None:
            return 0
        return row[0]

    def saveDatabase(self, county_item):
        county_val = (county_item.county_name, str(county_item.county_code))
        cursor = self.connection.cursor()
        cursor.execute(self.insert_county_query, county_val)
        self.connection.commit()

    def separateData(self):
        county_list = []
        list_temp_3 = []
        for index in range(len(self.county_name_column)):
            if self.county_name_column[index] in list_temp_3:
                continue
            else: 
                list_temp_3.append(self.county_name_column[index])
                county_list.append(CountyModel(self.county_name_column[index], self.county_code_column[index]))
        for county_item in county_list:
            if(pd.isna(county_item.county_name)):
                county_item.county_name = "null"

            if(pd.isna(county_item.county_code)):
                county_item.county_code = 0

            self.saveDatabase(county_item)
