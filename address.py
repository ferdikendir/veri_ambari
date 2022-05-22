from city import City
from country import Country
from county import County
import pandas as pd
import pyodbc
from us_forign import USForeign


class AddressModel:
    def __init__(self, street_address, city_id, state_id, country_id, county_id, us_foreign_id):
        self.street_address = street_address
        self.city_id = city_id
        self.state_id = state_id
        self.country_id = country_id
        self.county_id = county_id
        self.us_foreign_id = us_foreign_id


class Address:
    def createTable(self):
        cursor = self.connection.cursor()
        cursor.execute(self.create_table_sql)
        self.connection.commit()

    create_table_sql = '''
        CREATE TABLE Addresses (
            address_id int primary key IDENTITY(1,1) NOT FOR REPLICATION NOT NULL,
            street_address nvarchar(MAX),
            city_id int FOREIGN KEY REFERENCES Cities(city_id),
            state_id int FOREIGN KEY REFERENCES States(state_id),
            country_id int FOREIGN KEY REFERENCES Countries(country_id),
            county_id int FOREIGN KEY REFERENCES Counties(count_id),
            us_foreign_id int FOREIGN KEY REFERENCES US_Foreigns(us_foreign_id)
            )
            '''
    alter_table_sql = 'alter table Addresses'
    insert_address_query = "insert into Addresses (street_address, city_id, state_id, county_id, us_foreign_id) values (?, ?, ?, ?, ?)"
    get_address_by_id = "select address_id from Addresses where street_address=? and city_id=? and state_id=? and country_id=? and county_id=? and us_foreign_id=?"

    def __init__(self, street_address_column, city_code_column, city_name_column, state_code_column, state_name_column, county_code_column, county_name_column, us_foreign_name_column, connection):
        self.street_address_column = street_address_column
        self.city_code_column = city_code_column
        self.city_name_column = city_name_column
        self.state_code_column = state_code_column
        self.state_name_column = state_name_column
        self.county_code_column = county_code_column
        self.county_name_column = county_name_column
        self.us_foreign_name_column = us_foreign_name_column
        self.connection = connection
        #self.createTable()

    def saveDatabase(self, address_item):
        address_val = (address_item.street_address, int(address_item.city_id), int(address_item.state_id), int(
            address_item.country_id), int(address_item.county_id), int(address_item.us_foreign_id))
        cursor = self.connection.cursor()
        cursor.execute(self.insert_address_query, address_val)
        self.connection.commit()

    def separateData(self):
        address_list = []
        for index in range(len(self.street_address_column)):
            _state_id = State.getStateId(
                self.state_code_column[index], self.state_name_column[index])
            _city_id = City.getCityId(
                self.city_code_column[index], self.city_name_column[index])
            _county_id = County.getCountyId(
                self.county_code_column[index], self.county_name_column[index])
            _us_foreign_id = USForeign.getUSForeignId(
                self.us_foreign_name_column[index])
            address_list.append(AddressModel(
                self.street_address_column[index], _city_id, _state_id, _county_id, _us_foreign_id))
        for address_item in address_list:
            if(pd.isna(address_item.street_address)):
                address_item.street_address = "null"
            self.saveDatabase(address_item)
