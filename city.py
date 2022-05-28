import country as _country_
import pandas as pd

class CityModel:
    def __init__(self, city_code, city_name, zip_code, country_id): 
        self.city_code = city_code 
        self.city_name = city_name
        self.zip_code = zip_code
        self.country_id = country_id

class City:
    def createTable(self):
        cursor = self.connection.cursor()
        cursor.execute(self.create_table_sql)
        self.connection.commit()

    create_table_sql = '''
            CREATE TABLE Cities (
                city_id int primary key IDENTITY NOT NULL,
                city_name nvarchar(50),
                city_code nvarchar(50),
                zip_code nvarchar(50),
                country_id int,
                FOREIGN KEY (country_id) REFERENCES Countries(country_id)
                )
                '''
    table_name = 'Cities'
    insert_city_query = "insert into Cities (city_name, city_code, zip_code, country_id) values (?,?,?,?)"
    get_city_by_id = "select city_id from Cities where city_name=? and city_code=? and zip_code=? and country_id=?"

    
    def __init__(self, city_code_column, city_name_column, zip_code_column, country_name_column, country_code_column, connection): 
        self.city_code_column = city_code_column 
        self.city_name_column = city_name_column
        self.zip_code_column = zip_code_column
        self.country_name_column = country_name_column
        self.country_code_column = country_code_column
        self.connection = connection
        #self.createTable()

    def getCityId(self, city_name, city_code, zip_code, country_id):
        cursor = self.connection.cursor()
        cursor.execute(self.get_city_by_id, (city_name, int(city_code), str(zip_code), int(country_id)))
        result = cursor.fetchone()
        if result is None:
            return 0
        return result[0]

    def saveDatabase(self, city_item):
        city_val = (city_item.city_name, int(city_item.city_code), str(city_item.zip_code), int(city_item.country_id))
        cursor = self.connection.cursor()
        cursor.execute(self.insert_city_query, city_val)
        self.connection.commit()

    def separateData(self, country):
        city_list = []
        list_temp_4 = []

        for index in range(len(self.city_name_column)):
            if [self.city_name_column[index], self.city_code_column[index], self.zip_code_column[index]] in list_temp_4:
                continue
            else: 
                list_temp_4.append([self.city_name_column[index], self.city_code_column[index], self.zip_code_column[index]])
                country_id = country.getCountryId(self.country_name_column[index], self.country_code_column[index])
                city_list.append(CityModel(self.city_code_column[index], self.city_name_column[index], str(self.zip_code_column[index]) , int(country_id)))
                del country_id
        for city_item in city_list:
            if(pd.isna(city_item.city_name)):
                city_item.city_name = "null"

            if(pd.isna(city_item.city_code)):
                city_item.city_code = 0
            self.saveDatabase(city_item)