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
import mysql.connector

# connection = pyodbc.connect('Driver={ODBC Driver 17 for SQL Server};'
#                             'Server=RAST-MOBILE;'
#                             'Database=frpp_public;'
#                             'Trusted_Connection=yes;'
#                             )
connection = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  
  database="frpp_public"
)


frpp_public_ = pd.read_excel('frpp-public-dataset-fy2020-final-csv-1.xls')
frpp_public = frpp_public_

# --- Reporting Agency ---
_repornting_agency_obj = _reporting_agency.ReportingAgency(
    frpp_public['Reporting Agency Code'], frpp_public['Reporting Agency'], connection)
_repornting_agency_obj.separateData()

# ---- REPORTING BUREAU ----
_reporting_bureau_obj = _reporting_bureau.ReportingBureau(
    frpp_public['Reporting Bureau Code'], frpp_public['Reporting Bureau'], connection)
_reporting_bureau_obj.separateData()

# ---- USING AGENCY ----
_using_agency_obj = _using_agency.UsingAgency(
    frpp_public["Using Agency Code"], frpp_public["Using Agency"], connection)
_using_agency_obj.separateData()

# ---- USING BUREAU ----
_using_bureau_obj = _using_bureau.UsingBureau(
    frpp_public["Using Bureau Code"], frpp_public["Using Bureau"], connection)
_using_bureau_obj.separateData()

# ---- US/Foreign ----
_us_forign_obj = _us_forign.USForeign(frpp_public["US/Foreign"], connection)
_us_forign_obj.separateData()

# ---- County ----
_county_obj = _county.County(
    frpp_public["County Code"], frpp_public["County Name"], connection)
_county_obj.separateData()

# ---- Country ----
_country_obj = _country.Country(
    frpp_public["Country Code"], frpp_public["Country Name"], connection)
_country_obj.separateData()


# ---- City ----
_city_obj = _city.City(frpp_public["City Code"], frpp_public["City Name"],
                       frpp_public["Zip Code"], frpp_public["Country Name"], frpp_public["Country Code"], connection)
_city_obj.separateData(_country_obj)

# ---- State ----
_state_obj = _state.State(frpp_public["State Code"], frpp_public["State Name"], connection)
_state_obj.separateData()

# ---- Sub Installation ----
_sub_installation_obj = _sub_installation.SubInstallation(frpp_public["Sub Installation Id"], connection)
_sub_installation_obj.separateData()

# ---- Installation ----
_installation_obj = _installation.Installation(frpp_public["Installation Id"], frpp_public["Installation Name"], connection)
_installation_obj.separateData()

# ---- Real Property Type ----
_real_property_type_obj = _real_property_type.RealPropertyType(frpp_public["Real Property Type Code"], frpp_public["Real Property Type"], connection)
_real_property_type_obj.separateData()

# ---- Legal Interest ----
_legal_interest_obj = _legal_interest.LegalInterest(frpp_public["Legal Interest Indicator"], frpp_public["Legal Interest Code"], connection)
_legal_interest_obj.separateData()

# ---- Real Property Use ----
_real_property_use_obj = _real_property_use.RealPropertyUse(frpp_public["Real Property Use"], frpp_public["Real Property Use Code"], connection)
_real_property_use_obj.separateData()

# ---- Utilization ----
_utilization_obj = _utilization.Utilization(frpp_public["Utilization"], frpp_public["Utilization Code"], connection)
_utilization_obj.separateData()

# ---- Asset ----
_asset_obj = _asset.Asset(frpp_public["Asset Status"], frpp_public["Asset Status Code"], connection)
_asset_obj.separateData()

# ---- Historical Status ----
_historical_status_obj = _historical_status.HistoricalStatus(frpp_public["Historical Status"], connection)
_historical_status_obj.separateData()

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