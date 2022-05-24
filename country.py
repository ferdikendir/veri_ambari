import pandas as pd
import pyodbc
class CountryModel:
    def __init__(self, country_name, country_code):
        self.country_name = country_name
        self.country_code = country_code

class Country:
    def createTable(self):
        cursor = self.connection.cursor()
        cursor.execute(self.create_table_sql)
        self.connection.commit()

    create_table_sql = '''
            CREATE TABLE Countries (
                country_id int primary key AUTO_INCREMENT NOT NULL,
                country_name nvarchar(50),
                country_code nvarchar(50)
                );
                '''
    table_name = 'Countries'
    insert_country_query = "insert into Countries (country_name, country_code) values (%s, %s)"
    get_country_by_id = "select country_id from Countries where country_name=%s and country_code=%s"

    def __init__(self, code_column, name_column, connection):
        self.name_column = name_column
        self.code_column = code_column
        self.connection = connection
        self.createTable()

    def getCountryId(self, country_name, country_code):
        cursor = self.connection.cursor()
        cursor.execute(self.get_country_by_id, (country_name, int(country_code)))
        row = cursor.fetchone()
        if row is None:
            return 0
        return row[0]

    def saveDatabase(self, country_item):   
        bureau_val = (country_item.country_name, int(country_item.country_code))
        cursor = self.connection.cursor()
        cursor.execute(self.insert_country_query, bureau_val)
        self.connection.commit()

    def separateData(self):
        country_list = []
        country_names = self.name_column.unique()
        country_codes = self.code_column.unique()
        for i in range(len(country_names)):
            country_list.append(CountryModel(country_names[i], country_codes[i]))
        for country_item in country_list:
            if(pd.isna(country_item.country_name)):
                country_item.country_name = "null"

            if(pd.isna(country_item.country_code)):
                country_item.country_code = 0
            self.saveDatabase(country_item)

           