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
            
