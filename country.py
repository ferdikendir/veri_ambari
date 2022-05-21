import pandas as pd
class CountryModel:
    def __init__(self, country_name, country_code):
        self.country_name = country_name
        self.country_code = country_code

class Country:
    insert_country_query = "insert into Country (country_name, country_code) values (?,?)"
    def __init__(self, code_colum, name_column, connection):
        self.name_column = name_column
        self.code_colum = code_colum
        self.connection = connection

    def getCountryId(self):
        cursor = self.connection.cursor() 
        cursor.execute("select country_id from Country where country_name=? and country_code=?", self.country_name, int(self.country_code) )
        response = cursor.fetchall()
        self.connection.commit()
        return response[0][0] if response != [] else response

    def saveDatabase(self, country_item):
        cursor = self.connection.cursor()
        bureau_val = (country_item.country_name, int(country_item.country_code))
        cursor.execute(self.insert_country_query, bureau_val)
        self.connection.commit()

    def separateData(self):
        country_list = []
        country_names = self.name_column.unique()
        country_codes = self.code_colum.unique()
        for i in range(len(country_names)):
            country_list.append(CountryModel(country_names[i], country_codes[i]))
        for country_item in country_list:
            if(pd.isna(country_item.country_name)):
                country_item.country_name = "null"

            if(pd.isna(country_item.country_code)):
                country_item.country_code = 0
            self.saveDatabase(country_item)

           