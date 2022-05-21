from cmath import nan
import pyodbc 
import pandas as pd
import numpy as np

import reporting_agency as _reporting_agency

import reporting_bureau as _reporting_bureau

import using_agency as _using_agency

import using_bureau as _using_bureau

import us_forign as _us_forign

import country as _country

import county as _county

conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=RAST-MOBILE;'
                      'Database=frpp_public;'
                      'Trusted_Connection=yes;')

frpp_public = pd.read_excel('frpp-public-dataset-fy2020-final-csv-1.xls')

#--- Reporting Agency ---
_repornting_agency_obj = _reporting_agency.ReportingAgency(frpp_public['Reporting Agency Code'], frpp_public['Reporting Agency'], conn)
#_repornting_agency_obj.separateData()

# ---- REPORTING BUREAU ----
_reporting_bureau_obj = _reporting_bureau.ReportingBureau(frpp_public['Reporting Bureau Code'], frpp_public['Reporting Bureau'], conn)
#_reporting_bureau_obj.separateData()

#---- USING AGENCY ----
_using_agency_obj = _using_agency.UsingAgency(frpp_public["Using Agency Code"], frpp_public["Using Agency"], conn)
#_using_agency_obj.separateData()

# ---- USING BUREAU ----
_using_bureau_obj = _using_bureau.UsingBureau(frpp_public["Using Bureau Code"], frpp_public["Using Bureau"], conn)
#_using_bureau_obj.separateData()

#---- US/Foreign ----
_us_forign_obj = _us_forign.USForeign(frpp_public["US/Foreign"], conn)
#_us_forign_obj.separateData()

#---- Country ----
_country_obj = _country.Country(frpp_public["Country Code"], frpp_public["Country Name"], conn)
#_country_obj.separateData()

_county_obj = _county.County(frpp_public["County Code"], frpp_public["County Name"], conn)
_county_obj.separateData()


# class City:
#     def __init__(self, city_code, city_name, zip_code, country_id): 
#         self.city_code = city_code 
#         self.city_name = city_name
#         self.zip_code = zip_code
#         self.country_id = country_id

# insert_city_query = "insert into City (city_name, city_code, zip_code, country_id) values (?,?,?,?)"
# city_list = []
# list_temp_4 = []

# for index in range(len(frpp_public['City Name'])):
#     if frpp_public['City Name'][index] in list_temp_4 and frpp_public['City Code'][index] in list_temp_4 and frpp_public['Zip Code'][index] in list_temp_4:
#         continue
#     else: 
#         _country = Country( frpp_public['Country Code'][index], frpp_public['Country Name'][index])
#         list_temp_4.append([frpp_public['City Name'][index], frpp_public['City Code'][index], frpp_public['Zip Code'][index]])
#         city_list.append(City(frpp_public['City Code'][index], frpp_public['City Name'][index], frpp_public['Zip Code'], _country.getCountryId()))
#         del _country
# for city_item in city_list:
#     if(pd.isna(city_item.city_name)):
#         city_item.city_name = "null"

#     if(pd.isna(city_item.city_code)):
#         city_item.city_code = 0

#     cursor = conn.cursor()
#     city_val = (city_item.city_name, int(city_item.city_code), " ", city_item.country_id)
#     cursor.execute(insert_city_query, city_val)
#     conn.commit()

# class State:
#     def __init__(self, state_code, state_name): 
#         self.state_code = state_code 
#         self.state_name = state_name
# insert_state_query = "insert into State (state_name, state_code) values (?,?)"
# state_list = []
# list_temp_5 = []
# for index in range(len(frpp_public['State Name'])):
#     if frpp_public['State Name'][index] in list_temp_5:
#         continue
#     else: 
#         list_temp_5.append(frpp_public['State Name'][index])
#         state_list.append(State(frpp_public['State Code'][index], frpp_public['State Name'][index]))
# for state_item in state_list:
#     if(pd.isna(state_item.state_name)):
#         state_item.state_name = "null"

#     if(pd.isna(state_item.state_code)):
#         state_item.state_code = 0

#     cursor = conn.cursor()
#     state_val = (state_item.state_name, state_item.state_code)
#     cursor.execute(insert_state_query, state_val)
#     conn.commit()