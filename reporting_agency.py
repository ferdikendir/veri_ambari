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
        CREATE TABLE ReportingAgencies (
            agency_id int primary key IDENTITY(1,1) NOT FOR REPLICATION NOT NULL,
            agency_code nvarchar(50),
            agency_name nvarchar(50)
            )
            '''
    insert_agency_query = "insert into ReportingAgencies (agency_code, agency_name) values (?, ?)"
    get_agency_by_id = "select agency_id from ReportingAgencies where agency_code=? and agency_name=?"

    
    def __init__(self, agency_code_column, agency_name_column, connection):
        self.agency_code_column = agency_code_column 
        self.agency_name_column = agency_name_column
        self.connection = connection
        #self.createTable()

    def saveDatabase(self, reporting_agency_item):
        agency_val = (reporting_agency_item.agency_name, int(reporting_agency_item.agency_code))
        cursor = self.connection.cursor()
        cursor.execute(self.insert_agency_query, agency_val)
        self.connection.commit()

    def separateData(self):
        reporting_agency_list = []
        reporting_agency_names = self.agency_name_column.unique()
        reporting_agency_codes = self.agency_code_column.unique()
        for i in range(len(reporting_agency_names)):
            reporting_agency_list.append(ReportingAgencyModel(reporting_agency_codes[i], reporting_agency_names[i]))

        for reporting_agency_item in reporting_agency_list:
            self.saveDatabase(reporting_agency_item)
    