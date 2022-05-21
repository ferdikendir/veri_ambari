import _country as _country


class CityModel:
    def __init__(self, city_code, city_name, zip_code, country_id): 
        self.city_code = city_code 
        self.city_name = city_name
        self.zip_code = zip_code
        self.country_id = country_id
class City:
    insert_city_query = "insert into City (city_name, city_code, zip_code, country_id) values (?,?,?,?)"
    def __init__(self, city_code_column, city_name_column, zip_code_column, country_name_column, country_code_column, connection): 
        self.city_code_column = city_code_column 
        self.city_name_column = city_name_column
        self.zip_code_column = zip_code_column
        self.country_name_column = country_name_column
        self.country_code_column = country_code_column
        self.connection = connection

    def saveDatabase(self, city_item):
        cursor = self.connection.cursor()
        city_val = (city_item.city_name, int(city_item.city_code), city_item.zip_code, int(city_item.country_id))
        cursor.execute(self.insert_city_query, city_val)
        self.connection.commit()

    def separateData(self):
        city_list = []
        list_temp_4 = []

        for index in range(len(self.city_name_column)):
            if self.city_name_column[index] in list_temp_4 and self.city_code_column[index] in list_temp_4 and self.zip_code_column[index] in list_temp_4:
                continue
            else: 
                _country = _country.Country( self.country_code_column[index], self.country_name_column[index])
                list_temp_4.append([self.city_name_column[index], self.city_code_column[index], self.zip_code_column[index]])
                city_list.append(CityModel(self.city_code_column[index], self.city_name_column[index], self.zip_code_column[index] , _country.getCountryId()))
                del _country
        for city_item in city_list:
            if(pd.isna(city_item.city_name)):
                city_item.city_name = "null"

            if(pd.isna(city_item.city_code)):
                city_item.city_code = 0

            self.saveDatabase(city_item)