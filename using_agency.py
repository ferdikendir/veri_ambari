
import pandas as pd
class UsingAgencyModel: 
    def __init__(self, using_agency_code, using_agency_name): 
        self.using_agency_code = using_agency_code 
        self.using_agency_name = using_agency_name
        
class UsingAgency:
    insert_using_agency_query = "insert into UsingAgency (using_agency_name, using_agency_code) values (?,?)"
    
    def __init__(self, agency_code_column, agency_name_column, connection):
        self.agency_code_column = agency_code_column
        self.agency_name_column = agency_name_column
        self.connection = connection

    def saveDatabase(self, using_agency_item):
        cursor = self.connection.cursor()
        agency_val = (using_agency_item.using_agency_name, int(using_agency_item.using_agency_code))
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