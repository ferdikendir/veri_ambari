class ReportingBureauModel:
    def __init__(self, bureau_code, bureau_name): 
        self.bureau_code = bureau_code 
        self.bureau_name = bureau_name


class ReportingBureau:
    insert_reporting_bureau_query = "insert into ReportingBureau (reporting_bureau_name, reporting_bureau_code) values (?,?)"
    def __init__(self, bureau_code_column, bureau_name_column, connection): 
        self.bureau_code_column = bureau_code_column 
        self.bureau_name_column = bureau_name_column
        self.connection = connection

    def saveDatabase(self, reporting_bureau_item):
        cursor = self.connection.cursor()
        bureau_val = (reporting_bureau_item.bureau_name, int(reporting_bureau_item.bureau_code))
        cursor.execute(self.insert_reporting_bureau_query, bureau_val)
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