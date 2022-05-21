
class ReportingAgencyModel:
    def __init__(self, agency_code, agency_name): 
        self.agency_code = agency_code 
        self.agency_name = agency_name


    # ---- REPORTING AGENCY ----
class ReportingAgency:
    insert_reporting_agency_query = "insert into ReportingAgency (reporting_agency_name, reporting_agency_code) values (?,?)"
    def __init__(self, agency_code_column, agency_name_column, connection): 
        self.agency_code_column = agency_code_column 
        self.agency_name_column = agency_name_column
        self.connection = connection

    def saveDatabase(self, reporting_agency_item):
                cursor = self.connection.cursor()
                agency_val = (reporting_agency_item.agency_name, int(reporting_agency_item.agency_code))
                cursor.execute(self.insert_reporting_agency_query, agency_val)
                self.connection.commit()


    def separateData(self):
        reporting_agency_list = []
        reporting_agency_names = self.agency_name_column.unique()
        reporting_agency_codes = self.agency_code_column.unique()
        for i in range(len(reporting_agency_names)):
            reporting_agency_list.append(ReportingAgencyModel(reporting_agency_codes[i], reporting_agency_names[i]))

        for reporting_agency_item in reporting_agency_list:
            self.saveDatabase(reporting_agency_item)
    