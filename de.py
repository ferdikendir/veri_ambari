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

import city as _city

import state as _state

conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=RAST-MOBILE;'
                      'Database=frpp_public;'
                      'Trusted_Connection=yes;')

frpp_public = pd.read_excel('frpp-public-dataset-fy2020-final-csv-1.xls')
frpp_public = frpp_public.where(pd.notnull(frpp_public), None)
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

#---- County ----
_county_obj = _county.County(frpp_public["County Code"], frpp_public["County Name"], conn)
#_county_obj.separateData()

#---- City ----
_city_obj = _city.City(frpp_public["City Code"], frpp_public["City Name"], frpp_public["Zip Code"], frpp_public["Country Name"], frpp_public["Country Code"], conn)
_city_obj.separateData()

#---- State ----
_state_obj = _state.State(frpp_public["State Code"], frpp_public["State Name"], conn)
#_state_obj.separateData()