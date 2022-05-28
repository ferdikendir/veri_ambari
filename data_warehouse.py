from state import State
from city import City
from country import Country
from county import County
import pandas as pd
import pyodbc
from us_forign import USForeign


class AddressModel:
    def __init__(self, street_address, city_id, state_id, country_id, 
    county_id, us_foreign_id, sub_installation_id, installation_id, reporting_agency_id,
     reporting_bureau_id, using_agency_id, using_bureau_id, real_property_type_id, 
     real_property_use_id, latitude, longitude):
        self.street_address = street_address
        self.city_id = city_id
        self.state_id = state_id
        self.country_id = country_id
        self.county_id = county_id
        self.us_foreign_id = us_foreign_id
        self.sub_installation_id = sub_installation_id
        self.installation_id = installation_id
        self.reporting_agency_id = reporting_agency_id
        self.reporting_bureau_id = reporting_bureau_id
        self.using_agency_id = using_agency_id
        self.using_bureau_id = using_bureau_id
        self.real_property_type_id = real_property_type_id
        self.real_property_use_id = real_property_use_id
        self.latitude = latitude
        self.longitude = longitude


class Address:
    def createTable(self):
        cursor = self.connection.cursor()
        cursor.execute(self.create_table_sql)
        self.connection.commit()

    create_table_sql = '''
            CREATE TABLE Addresses (
            address_id int primary key IDENTITY NOT NULL,
            street_address nvarchar(max),
            city_id int,
            state_id int,
            country_id int,
            county_id int,
            us_foreign_id int,
            installation_id int,
            reporting_agency_id int,
            reporting_bureau_id int,
            using_agency_id int,
            using_bureau_id int,
            real_property_id int,
            real_property_type_id int,
            latitude nvarchar(50),
            longitude nvarchar(50),
            legal_interest_id int,
            utilization_id int,
            asset_id int,
            historical_id int
            )
            '''
    alter_table_sql = 'alter table Addresses'
    insert_address_query = '''INSERT INTO  addresses( street_address ,  city_id ,  state_id ,  country_id , 
     county_id ,  us_foreign_id ,  installation_id ,  reporting_agency_id , 
     reporting_bureau_id ,  using_agency_id ,  using_bureau_id ,  real_property_id ,  real_property_type_id ,
     latitude ,  longitude ,  legal_interest_id ,  utilization_id ,  asset_id ,  historical_id )
     VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)'''

    get_address_by_id = "select address_id from Addresses where street_address=? and city_id=? and state_id=? and country_id=? and county_id=? and us_foreign_id=? and installation_id=? and sub_installation_id=? and reporting_agency_id=? and reporting_bureau_id=? and using_agency_id=? and using_bureau_id=? and real_property_id=? and real_property_type_id=?"

    def __init__(self, street_address_column, latitude_column, longitude_column, connection):
        self.street_address_column = street_address_column
        self.latitude_column = latitude_column
        self.longitude_column = longitude_column
        self.connection = connection
        self.createTable()

    def saveDatabase(self, street_address, city_id, state_id, country_id, 
    county_id, us_foreign_id, installation_id, reporting_agency_id,
     reporting_bureau_id, using_agency_id, using_bureau_id, real_property_type_id, 
     real_property_use_id, latitude, longitude, _legal_interest, utilization_id, asset_id, historical_id):
        cursor = self.connection.cursor()
        cursor.execute(self.insert_address_query, (str(street_address),
                                                   int(city_id),
                                                   int(state_id),
                                                   int(country_id),
                                                   int(county_id),
                                                   int(us_foreign_id),
                                                   int(installation_id),
                                                   int(reporting_agency_id),
                                                   int(reporting_bureau_id),
                                                   int(using_agency_id),
                                                   int(using_bureau_id),
                                                   int(real_property_use_id),
                                                   int(real_property_type_id),
                                                   str(latitude), str(longitude),
                                                   int(_legal_interest),
                                                   int(utilization_id),
                                                   int(asset_id),
                                                   int(historical_id), ))
        self.connection.commit()

    def separateData(self, city, state, country, county, us_foreign, installation, sub_installation,
    reporting_agency, reporting_bureau, using_agency, using_bureau, real_property,
    real_property_type, legal_interest_obj, utilization_obj, asset_obj, historical_obj):
        for i in range(len( self.street_address_column)):
            index =  i
            _country = country.getCountryId(
                country.name_column[index], country.code_column[index])
            _state = state.getStateId(
                state.state_name_column[index], state.state_code_column[index])
            _city = city.getCityId(
                city.city_name_column[index], city.city_code_column[index], city.zip_code_column[index], _country)
            _county = county.getCountyId(
                county.county_name_column[index], str(county.county_code_column[index]))
            _us_foreign = us_foreign.getUSForeignId(
                us_foreign.us_forign_name[index])
            _installation = installation.getInstallationId(
                installation.installation_code_column[index], installation.installation_name_column[index])
            _sub_installation = sub_installation.getSubInstallationId(
                sub_installation.sub_installation_code_column[index])
            _reporting_agency = reporting_agency.getReportingAgencyId(
                reporting_agency.agency_code_column[index], reporting_agency.agency_name_column[index])
            _reporting_bureau = reporting_bureau.getReportingBureauId(
                reporting_bureau.bureau_code_column[index], reporting_bureau.bureau_name_column[index])
            _using_agency = using_agency.getUsingAgencyId(
                using_agency.agency_code_column[index], using_agency.agency_name_column[index])
            _using_bureau = using_bureau.getBureauId(
                using_bureau.bureau_code_column[index], using_bureau.bureau_name_column[index])
            _real_property = real_property.getRealPropertyUseId(
                real_property.name_column[index], real_property.code_column[index])
            _real_property_type = real_property_type.getRealPropertyTypeId(
                real_property_type.real_property_code_column[index], real_property_type.real_property_name_column[index])
            _street_address = self.street_address_column[index]
            latitude = self.latitude_column[index]
            longitude = self.longitude_column[index]
            _utilization = utilization_obj.getUtilizationId(utilization_obj.utilization_column[index], utilization_obj.utilization_code_column[index])
            _legal_interest = legal_interest_obj.getLegalInterestId(legal_interest_obj.name_column[index], legal_interest_obj.code_column[index])
            _asset = asset_obj.getAssetId(asset_obj.asset_status_column[index], asset_obj.asset_status_code_column[index])
            _historical = historical_obj.getHistoricalStatusId(historical_obj.historical_status_column[index])
            self.saveDatabase(_street_address, _city, _state, _country, _county, _us_foreign, _installation,
                                        _reporting_agency, _reporting_bureau, _using_agency, 
                                        _using_bureau, _real_property, _real_property_type, 
                                        latitude, longitude, _legal_interest, _utilization, _asset, _historical)
            

class AssetModel:
    def __self__(self, asset_status, asset_status_code):
        self.asset_status = asset_status
        self.asset_status_code = asset_status_code

class Asset:
    def createTable(self):
        cursor = self.connection.cursor()
        cursor.execute(self.create_table_sql)
        self.connection.commit()

    create_table_sql = '''      CREATE TABLE Assets (
            asset_id int primary key IDENTITY NOT NULL,
            asset_status nvarchar(250),
            asset_status_code nvarchar(250)
            );
            '''
    table_name = "Assets"
    insert_asset_query = "insert into Assets (asset_status, asset_status_code) values (?, ?)"
    get_asset_by_id = "select asset_id from Assets where asset_status=? and asset_status_code=?"

    def __init__(self, asset_status_column, asset_status_code_column, connection):
        self.asset_status_column = asset_status_column
        self.asset_status_code_column = asset_status_code_column
        self.connection = connection
        #self.createTable()

    def getAssetId(self, asset_status, asset_status_code):
        cursor = self.connection.cursor()
        cursor.execute(self.get_asset_by_id, (asset_status, asset_status_code))
        asset_id = cursor.fetchone()
        return asset_id[0]

    def saveDatabase(self, asset_item):
        cursor = self.connection.cursor()
        cursor.execute(self.insert_asset_query, asset_item)
        self.connection.commit()

    def separateData(self):
        asset_list =  []
        for index in  range(len(self.asset_status_column)):
            if self.asset_status_column[index] in asset_list:
                continue
            else:
                asset_list.append(self.asset_status_column[index])
                asset_item = (str(self.asset_status_column[index]), str(self.asset_status_code_column[index]))
                self.saveDatabase(asset_item)
    
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
                country_id int primary key IDENTITY NOT NULL,
                country_name nvarchar(50),
                country_code nvarchar(50)
                );
                '''
    table_name = 'Countries'
    insert_country_query = "insert into Countries (country_name, country_code) values (?, ?)"
    get_country_by_id = "select country_id from Countries where country_name=? and country_code=?"

    def __init__(self, code_column, name_column, connection):
        self.name_column = name_column
        self.code_column = code_column
        self.connection = connection
        #self.createTable()

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
class HistoricalStatus:
    def createTable(self):
        cursor = self.connection.cursor()
        cursor.execute(self.create_table_sql)
        self.connection.commit()

    create_table_sql = '''        CREATE TABLE HistoricalStatuses (
            historical_status_id int primary key IDENTITY NOT NULL,
            historical_status nvarchar(250)
            );
            '''
    table_name = "HistoricalStatuses"
    insert_historical_status_query = "insert into HistoricalStatuses (historical_status) values (?)"
    get_historical_status_by_id = "select historical_status_id from HistoricalStatuses where historical_status=?"

    def __init__(self, historical_status_column, connection):
        self.historical_status_column = historical_status_column
        self.connection = connection
        #self.createTable()

    def getHistoricalStatusId(self, historical_status):
        cursor = self.connection.cursor()
        cursor.execute(self.get_historical_status_by_id, str(historical_status))
        historical_status_id = cursor.fetchone()
        return historical_status_id[0]

    def saveDatabase(self, historical_status_item):
        cursor = self.connection.cursor()
        cursor.execute(self.insert_historical_status_query, (historical_status_item, ))
        self.connection.commit()

    def separateData(self):
        _historical_status_list = self.historical_status_column.unique()
        for index in range(len(_historical_status_list)):
            self.saveDatabase(_historical_status_list[index])

class InstallationModel:
    def __init__(self, installation_code, installation_name): 
        self.installation_code = installation_code 
        self.installation_name = installation_name


class Installation:
    def createTable(self):
        cursor = self.connection.cursor()
        cursor.execute(self.create_table_sql)
        self.connection.commit()

    create_table_sql = '''        CREATE TABLE Installations (
            installation_id int primary key IDENTITY NOT NULL,
            installation_name nvarchar(250),
            installation_code nvarchar(250)
            );
            '''
    table_name = "Installations"
    insert_installation_query = "insert into Installations (installation_name, installation_code) values (?, ?)"
    get_installation_by_id = "select installation_id from Installations where installation_code=? and installation_name=?"

    def __init__(self, installation_code_column, installation_name_column, connection):
        self.installation_code_column = installation_code_column 
        self.installation_name_column = installation_name_column
        self.connection = connection
        #self.createTable()

    def getInstallationId(self, installation_code, installation_name):
        cursor = self.connection.cursor()
        cursor.execute(self.get_installation_by_id, (str(installation_code), str(installation_name)))
        installation_id = cursor.fetchone()
        if installation_id is None:
            return 0
        return installation_id[0]

    def saveDatabase(self, name, code):
        cursor = self.connection.cursor()
        cursor.execute(self.insert_installation_query, (name, str(code)))
        self.connection.commit()

    def separateData(self):
        installation_list = []
        list = []
        for index in range(len(self.installation_name_column)):
            if self.installation_code_column[index] in list:
                continue
            else: 
                list.append(self.installation_code_column[index])
                self.saveDatabase(self.installation_name_column[index], self.installation_code_column[index])

class LegalInterestModel:
    def __init__(self, name, code):
        self.name = name
        self.code = code

class LegalInterest:
    def createTable(self):
        cursor = self.connection.cursor()
        cursor.execute(self.create_table_sql)
        self.connection.commit()

    create_table_sql = '''      CREATE TABLE LegalInterests (
            legal_interest_id int primary key IDENTITY NOT NULL,
            name nvarchar(250),
            code nvarchar(250)
            );
            '''
    table_name = "LegalInterests"
    insert_legal_interest_query = "insert into LegalInterests (name, code) values (?, ?)"
    get_legal_interest_by_id = "select legal_interest_id from LegalInterests where name=? and code=?"

    def __init__(self, name_column, code_column, connection):
        self.name_column = name_column
        self.code_column = code_column
        self.connection = connection
        #self.createTable()

    def getLegalInterestId(self, name, code):
        cursor = self.connection.cursor()
        cursor.execute(self.get_legal_interest_by_id, (name, str(code)))
        legal_interest_id = cursor.fetchone()
        return legal_interest_id[0]

    def saveDatabase(self, legal_interest_item):
        cursor = self.connection.cursor()
        cursor.execute(self.insert_legal_interest_query, legal_interest_item)
        self.connection.commit()

    def separateData(self):
        legal_interest_name_list =  self.name_column.unique()
        legal_interest_code_list =  self.code_column.unique()
        for index in  range(len(legal_interest_name_list)):
            legal_interest_item = (str(legal_interest_name_list[index]), str(legal_interest_code_list[index]))
            self.saveDatabase(legal_interest_item)

class RealPropertyTypeModel:
    def __init__(self, real_property_code, real_property_name):
        self.real_property_code = real_property_code
        self.real_property_name = real_property_name

class RealPropertyType:
    def createTable(self):
        cursor = self.connection.cursor()
        cursor.execute(self.create_table_sql)
        self.connection.commit()

    create_table_sql = '''        CREATE TABLE RealPropertyTypes (
            real_property_type_id int primary key IDENTITY NOT NULL,
            real_property_code nvarchar(250),
            real_property_name nvarchar(250)
            );
            '''
    table_name = "RealPropertyTypes"
    insert_real_property_type_query = "insert into RealPropertyTypes (real_property_code, real_property_name) values (?, ?)"
    get_real_property_type_by_id = "select real_property_type_id from RealPropertyTypes where real_property_code=? and real_property_name=?"

    def __init__(self, real_property_code_column, real_property_name_column, connection):
        self.real_property_code_column = real_property_code_column
        self.real_property_name_column = real_property_name_column
        self.connection = connection
        #self.createTable()

    def getRealPropertyTypeId(self, real_property_code, real_property_name):    
        cursor = self.connection.cursor()
        cursor.execute(self.get_real_property_type_by_id, (str(real_property_code), real_property_name))
        real_property_type_id = cursor.fetchone()
        if real_property_type_id is None:
            return 0
        return real_property_type_id[0]

    def saveDatabase(self, real_property_type_item):
        cursor = self.connection.cursor()
        cursor.execute(self.insert_real_property_type_query, real_property_type_item)
        self.connection.commit()

    def separateData(self):
        real_property_type_code_list =  self.real_property_code_column.unique()
        real_property_type_name_list =  self.real_property_name_column.unique()
        for index in  range(len(real_property_type_code_list)):
            real_property_type_item = (str(real_property_type_code_list[index]), real_property_type_name_list[index])
            self.saveDatabase(real_property_type_item)

class RealPropertyUseModel:
    def __init__(self, name, code):
        self.name = name
        self.code = code

class RealPropertyUse:
    def createTable(self):
        cursor = self.connection.cursor()
        cursor.execute(self.create_table_sql)
        self.connection.commit()
    create_table_sql = '''        CREATE TABLE RealPropertyUses (
            real_property_use_id int primary key IDENTITY NOT NULL,
            name nvarchar(250),
            code nvarchar(250)
            );
            '''
    table_name = "RealPropertyUses"
    insert_real_property_use_query = "insert into RealPropertyUses (name, code) values (?, ?)"
    get_real_property_use_by_id = "select real_property_use_id from RealPropertyUses where name=? and code=?"
    def __init__(self, name_column, code_column, connection):
        self.name_column = name_column
        self.code_column = code_column
        self.connection = connection
        #self.createTable()

    def getRealPropertyUseId(self, name, code):    
        cursor = self.connection.cursor()
        cursor.execute(self.get_real_property_use_by_id, (name, str(code)))
        real_property_use_id = cursor.fetchone()
        if real_property_use_id is None:
            return 0
        return real_property_use_id[0]

    def saveDatabase(self, real_property_use_item):
        cursor = self.connection.cursor()
        cursor.execute(self.insert_real_property_use_query, (real_property_use_item.name, real_property_use_item.code))
        self.connection.commit()

    def separateData(self):
        real_property_use_list = []
        list_temp_2 = []
        for index in range(len(self.name_column)):
            if self.name_column[index] in list_temp_2:
                continue
            else: 
                list_temp_2.append(self.name_column[index])
                real_property_use_list.append(RealPropertyUseModel(self.name_column[index], str(self.code_column[index])))
        for real_property_use_item in real_property_use_list:
            self.saveDatabase(real_property_use_item)

import pyodbc


class ReportingAgencyModel:
    def __init__(self, agency_code, agency_name):
        self.agency_code = agency_code
        self.agency_name = agency_name


class ReportingAgency:
    def createTable(self):
        cursor = self.connection.cursor()
        cursor.execute(self.create_table_sql)
        self.connection.commit()

    create_table_sql = '''
        CREATE TABLE ReportingAgencies ( agency_id int primary key IDENTITY NOT NULL, agency_code nvarchar(50), 
            agency_name nvarchar(50) )
            '''
    insert_agency_query = "insert into ReportingAgencies (agency_name, agency_code) values (?, ?)"
    get_agency_by_id = "select agency_id from ReportingAgencies where agency_code=? and agency_name=?"

    def __init__(self, agency_code_column, agency_name_column, connection):
        self.agency_code_column = agency_code_column
        self.agency_name_column = agency_name_column
        self.connection = connection
        # self.createTable()

    def getReportingAgencyId(self, agency_code, agency_name):
        cursor = self.connection.cursor()
        cursor.execute(self.get_agency_by_id, (str(agency_code), agency_name))
        agency_id = cursor.fetchone()
        if agency_id is None:
            return 0
        return agency_id[0]

    def saveDatabase(self, reporting_agency_item):
        agency_val = (reporting_agency_item.agency_name,
                      int(reporting_agency_item.agency_code))
        cursor = self.connection.cursor()
        cursor.execute(self.insert_agency_query, agency_val)
        self.connection.commit()

    def separateData(self):
        reporting_agency_list = []
        reporting_agency_names = self.agency_name_column.unique()
        reporting_agency_codes = self.agency_code_column.unique()
        for i in range(len(reporting_agency_names)):
            reporting_agency_list.append(ReportingAgencyModel(
                reporting_agency_codes[i], reporting_agency_names[i]))

        for reporting_agency_item in reporting_agency_list:
            self.saveDatabase(reporting_agency_item)

class ReportingBureauModel:
    def __init__(self, bureau_code, bureau_name): 
        self.bureau_code = bureau_code 
        self.bureau_name = bureau_name

class ReportingBureau:
    def createTable(self):
        cursor = self.connection.cursor()
        cursor.execute(self.create_table_sql)
        self.connection.commit()

    create_table_sql = '''        CREATE TABLE ReportingBureaus (
            bureau_id int primary key IDENTITY NOT NULL,
            bureau_code nvarchar(50),
            bureau_name nvarchar(50)
            );
            '''
    table_name = "ReportingBureaus"
    insert_bureau_query = "insert into ReportingBureaus (bureau_name, bureau_code) values (?, ?)"
    get_bureau_by_id = "select bureau_id from ReportingBureaus where bureau_code=? and bureau_name=?"

    def __init__(self, bureau_code_column, bureau_name_column, connection):
        self.bureau_code_column = bureau_code_column 
        self.bureau_name_column = bureau_name_column
        self.connection = connection
        #self.createTable()

    def saveDatabase(self, reporting_bureau_item):
        bureau_val = (reporting_bureau_item.bureau_name, int(reporting_bureau_item.bureau_code))
        cursor = self.connection.cursor()
        cursor.execute(self.insert_bureau_query, bureau_val)
        self.connection.commit()

    def getReportingBureauId(self, bureau_code, bureau_name):
        cursor = self.connection.cursor()
        cursor.execute(self.get_bureau_by_id, (int(bureau_code), bureau_name))
        bureau_id = cursor.fetchone()
        if bureau_id is None:
            return 0
        return bureau_id[0]
    
    def separateData(self):
        reporting_bureau_list = []
        list = []
        for index in range(len(self.bureau_name_column)):
            if self.bureau_name_column[index] in list:
                continue
            else: 
                list.append(self.bureau_name_column[index])
                reporting_bureau_list.append(ReportingBureauModel(self.bureau_code_column[index], self.bureau_name_column[index]))
        for reporting_bureau_item in reporting_bureau_list:
            self.saveDatabase(reporting_bureau_item)

import pandas as pd
import pyodbc
class StateModel:
    def __init__(self, state_code, state_name):
        self.state_name = state_name
        self.state_code = state_code

class State:
    def createTable(self):
        cursor = self.connection.cursor()
        cursor.execute(self.create_table_sql)
        self.connection.commit()
    create_table_sql = '''            CREATE TABLE States (
                state_id int primary key IDENTITY NOT NULL,
                state_name nvarchar(50),
                state_code nvarchar(50)
                );
                '''
    table_name = 'States'
    insert_state_query = "insert into States (state_name, state_code) values (?, ?)"
    get_state_by_id = "select state_id from States where state_name=? and state_code=?"


    def __init__(self, state_code_column, state_name_column, connection):
        self.state_code_column = state_code_column
        self.state_name_column = state_name_column
        self.connection = connection
        #self.createTable()

    def getStateId(self, state_name, state_code):
        cursor = self.connection.cursor()
        cursor.execute(self.get_state_by_id, (state_name, str(state_code)))
        row = cursor.fetchone()
        if row is None:
            return 0
        return row[0]

    def saveDatabase(self, state_item):
        state_val = (state_item.state_name, str(state_item.state_code))
        cursor = self.connection.cursor()
        cursor.execute(self.insert_state_query, state_val)
        self.connection.commit()

    def separateData(self):
        state_list = []
        list_temp_5 = []
        for index in range(len(self.state_name_column)):
            if self.state_name_column[index] in list_temp_5:
                continue
            else: 
                list_temp_5.append(self.state_name_column[index])
                state_list.append(StateModel(self.state_code_column[index], self.state_name_column[index]))
        for state_item in state_list:
            if(pd.isna(state_item.state_name)):
                state_item.state_name = "null"

            if(pd.isna(state_item.state_code)):
                state_item.state_code = 0
            self.saveDatabase(state_item)

import pandas as pd
class USForeignModel:
    def __init__(self, us_forign_name):
        self.us_foreign_name = us_forign_name

class USForeign:
    def createTable(self):
        cursor = self.connection.cursor()
        cursor.execute(self.create_table_sql)
        self.connection.commit()

    create_table_sql = '''           CREATE TABLE US_Foreigns (
                us_foreign_id int primary key IDENTITY NOT NULL,
                us_foreign_name nvarchar(50)
                );
                '''
    table_name = 'USForeigns'
    insert_us_forign_query = "insert into US_Foreigns (us_foreign_name) values (?)"
    get_us_forign_by_id = "select us_foreign_id from US_Foreigns where us_foreign_name=?"

    def __init__(self, us_forign_name, connection):
        self.us_forign_name = us_forign_name
        self.connection = connection
        #self.createTable()

    def getUSForeignId(self, us_foreign_name):
        cursor = self.connection.cursor()
        cursor.execute(self.get_us_forign_by_id, (us_foreign_name,))
        us_foreign_id = cursor.fetchone()
        if us_foreign_id is None:
            return 0
        return us_foreign_id[0]

    def saveDatabase(self, us_foreign_name):
        cursor = self.connection.cursor()
        cursor.execute(self.insert_us_forign_query, (str(us_foreign_name), ))
        self.connection.commit()

    def separateData(self):
        us_foreign_list = []
        us_foreign_names = self.us_forign_name.unique()
        for i in range(len(us_foreign_names)):
            if(pd.isna(us_foreign_names[i])):
                us_foreign_names[i] = "null"
            self.saveDatabase(us_foreign_names[i])


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
        
import pandas as pd
import pyodbc

class UsingBureauModel:
    def __init__(self, bureau_name, bureau_code):
        self.bureau_code = bureau_code
        self.bureau_name = bureau_name


class UsingBureau:
    create_table_sql = '''         CREATE TABLE UsingBureaus (
            bureau_id int primary key IDENTITY NOT NULL,
            bureau_code nvarchar(50),
            bureau_name nvarchar(50)
            );
            '''
    table_name = 'UsingBureaus'
    insert_bureau_query = "insert into UsingBureaus (bureau_name, bureau_code) values (?, ?)"
    get_bureau_by_id = "select bureau_id from UsingBureaus where bureau_code=? and bureau_name=?"

    def createTable(self):
        cursor = self.connection.cursor()
        cursor.execute(self.create_table_sql)
        self.connection.commit()

    def __init__(self, bureau_code_column, bureau_name_column, connection):
        self.bureau_name_column = bureau_name_column
        self.bureau_code_column = bureau_code_column
        self.connection = connection
        #self.createTable()

    def getBureauId(self, bureau_code, bureau_name):
        cursor = self.connection.cursor()
        cursor.execute(self.get_bureau_by_id, (str(bureau_code), bureau_name))
        bureau_id = cursor.fetchone()
        if bureau_id is None:
            return 0
        return bureau_id[0]

    def saveDatabase(self, using_bureau_item):
        using_bureau_val = (using_bureau_item.bureau_name, str(using_bureau_item.bureau_code))
        cursor = self.connection.cursor()
        cursor.execute(self.insert_bureau_query, using_bureau_val)
        self.connection.commit()

    def separateData(self):
        using_bureau_list = []
        list_temp_2 = []
        for index in range(len(self.bureau_name_column)):
            if self.bureau_name_column[index] in list_temp_2:
                continue
            else: 
                list_temp_2.append(self.bureau_name_column[index])
                using_bureau_list.append(UsingBureauModel(self.bureau_name_column[index], self.bureau_code_column[index]))
        for using_bureau_item in using_bureau_list:
            if(pd.isna(using_bureau_item.bureau_name)):
               using_bureau_item.bureau_name = "null"
            if(pd.isna(using_bureau_item.bureau_code)):
               using_bureau_item.bureau_code = 0
            self.saveDatabase(using_bureau_item)

class UtilizationModel:
    def __init__(self,
                 utilization,
                 utilization_code):
        self.utilization = utilization
        self.utilization_code = utilization_code

class Utilization:
    def createTable(self):
        cursor = self.connection.cursor()
        cursor.execute(self.create_table_sql)
        self.connection.commit()

    create_table_sql = '''      CREATE TABLE Utilizations (
            utilization_id int primary key IDENTITY NOT NULL,
            utilization nvarchar(250),
            utilization_code nvarchar(250)
            );
            '''
    table_name = "Utilizations"
    insert_utilization_query = "insert into Utilizations (utilization, utilization_code) values (?, ?)"
    get_utilization_by_id = "select utilization_id from Utilizations where utilization=? and utilization_code=?"

    def __init__(self, utilization_column, utilization_code_column, connection):
        self.utilization_column = utilization_column
        self.utilization_code_column = utilization_code_column
        self.connection = connection
        #self.createTable()

    def getUtilizationId(self, utilization, utilization_code):
        cursor = self.connection.cursor()
        cursor.execute(self.get_utilization_by_id, (utilization, str(utilization_code)))
        utilization_id = cursor.fetchone()
        return utilization_id[0]

    def saveDatabase(self, utilization_item):
        cursor = self.connection.cursor()
        cursor.execute(self.insert_utilization_query, (utilization_item))
        self.connection.commit()

    def separateData(self):
        _utilization_list = []
        for index in range(len(self.utilization_column)):
            if self.utilization_column[index] in _utilization_list:
                continue
            else:
                _utilization_list.append(self.utilization_column[index])
                utilization_item = (str(self.utilization_column[index]), str(self.utilization_code_column[index]))
                self.saveDatabase(utilization_item)

import pandas as pd

import reporting_agency as _reporting_agency

import reporting_bureau as _reporting_bureau

import using_agency as _using_agency

import using_bureau as _using_bureau

import us_forign as _us_forign

import country as _country

import county as _county

import city as _city

import state as _state

import address as _address

import installation as _installation

import sub_installation as _sub_installation

import real_property_type as _real_property_type

import legal_interest as _legal_interest

import real_property_use as _real_property_use

import utilization as _utilization

import asset as _asset

import historical_status as _historical_status

import pyodbc

connection = pyodbc.connect('Driver={ODBC Driver 17 for SQL Server};'
                            'Server=RAST-MOBILE;'
                            'Database=frpp_public;'
                            'Trusted_Connection=yes;'
                            )


frpp_public = pd.read_excel('frpp-public-dataset-fy2020-final-csv-1.xls')

# --- Reporting Agency ---
_repornting_agency_obj = _reporting_agency.ReportingAgency(
    frpp_public['Reporting Agency Code'], frpp_public['Reporting Agency'], connection)
#_repornting_agency_obj.separateData()

# ---- REPORTING BUREAU ----
_reporting_bureau_obj = _reporting_bureau.ReportingBureau(
    frpp_public['Reporting Bureau Code'], frpp_public['Reporting Bureau'], connection)
#_reporting_bureau_obj.separateData()

# ---- USING AGENCY ----
_using_agency_obj = _using_agency.UsingAgency(
    frpp_public["Using Agency Code"], frpp_public["Using Agency"], connection)
#_using_agency_obj.separateData()

# ---- USING BUREAU ----
_using_bureau_obj = _using_bureau.UsingBureau(
    frpp_public["Using Bureau Code"], frpp_public["Using Bureau"], connection)
#_using_bureau_obj.separateData()

# ---- US/Foreign ----
_us_forign_obj = _us_forign.USForeign(frpp_public["US/Foreign"], connection)
#_us_forign_obj.separateData()

# ---- County ----
_county_obj = _county.County(
    frpp_public["County Code"], frpp_public["County Name"], connection)
#_county_obj.separateData()

# ---- Country ----
_country_obj = _country.Country(
    frpp_public["Country Code"], frpp_public["Country Name"], connection)
#_country_obj.separateData()


# ---- City ----
_city_obj = _city.City(frpp_public["City Code"], frpp_public["City Name"],
                       frpp_public["Zip Code"], frpp_public["Country Name"], frpp_public["Country Code"], connection)
#_city_obj.separateData(_country_obj)

# ---- State ----
_state_obj = _state.State(frpp_public["State Code"], frpp_public["State Name"], connection)
#_state_obj.separateData()

# ---- Sub Installation ----
_sub_installation_obj = _sub_installation.SubInstallation(frpp_public["Sub Installation Id"], connection)
#_sub_installation_obj.separateData()

# ---- Installation ----
_installation_obj = _installation.Installation(frpp_public["Installation Id"], frpp_public["Installation Name"], connection)
#_installation_obj.separateData()

# ---- Real Property Type ----
_real_property_type_obj = _real_property_type.RealPropertyType(frpp_public["Real Property Type Code"], frpp_public["Real Property Type"], connection)
#_real_property_type_obj.separateData()

# ---- Legal Interest ----
_legal_interest_obj = _legal_interest.LegalInterest(frpp_public["Legal Interest Indicator"], frpp_public["Legal Interest Code"], connection)
#_legal_interest_obj.separateData()

# ---- Real Property Use ----
_real_property_use_obj = _real_property_use.RealPropertyUse(frpp_public["Real Property Use"], frpp_public["Real Property Use Code"], connection)
#_real_property_use_obj.separateData()

# ---- Utilization ----
_utilization_obj = _utilization.Utilization(frpp_public["Utilization"], frpp_public["Utilization Code"], connection)
#_utilization_obj.separateData()

# ---- Asset ----
_asset_obj = _asset.Asset(frpp_public["Asset Status"], frpp_public["Asset Status Code"], connection)
#_asset_obj.separateData()

# ---- Historical Status ----
_historical_status_obj = _historical_status.HistoricalStatus(frpp_public["Historical Status"], connection)
#_historical_status_obj.separateData()

# ---- Address ----
_address_obj = _address.Address(
    frpp_public["Street Address"], frpp_public["Latitude"], frpp_public["Longitude"], connection)
_address_obj.separateData(
    _city_obj, 
_state_obj,
_country_obj, _county_obj,
   _us_forign_obj, 
_installation_obj, 
_sub_installation_obj, 
 _repornting_agency_obj, 
 _reporting_bureau_obj,
  _using_agency_obj,
   _using_bureau_obj,
    _real_property_use_obj,
   _real_property_type_obj, _legal_interest_obj, _utilization_obj, _asset_obj, _historical_status_obj)