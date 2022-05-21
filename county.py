import pandas as pd
class CountyModel:
    def __init__(self, county_name, county_code):
        self.county_name = county_name
        self.county_code = county_code

class County:
    insert_county_query = "insert into County (county_name, county_code) values (?,?)"
    def __init__(self, county_code_column, county_name_column, connection):
        self.county_code_column = county_code_column
        self.county_name_column = county_name_column
        self.connection = connection

    def saveDatabase(self, county_item):
        cursor = self.connection.cursor()
        county_val = (county_item.county_name, int(county_item.county_code))
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
