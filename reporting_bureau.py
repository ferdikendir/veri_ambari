class ReportingBureauModel:
    def __init__(self, bureau_code, bureau_name): 
        self.bureau_code = bureau_code 
        self.bureau_name = bureau_name

class ReportingBureau:
    def createTable(self):
        cursor = self.connection.cursor()
        cursor.execute(self.create_table_sql)
        self.connection.commit()

    create_table_sql = '''
        CREATE TABLE ReportingBureaus (
            bureau_id int primary key IDENTITY(1,1) NOT FOR REPLICATION NOT NULL,
            bureau_code nvarchar(50),
            bureau_name nvarchar(50)
            )
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