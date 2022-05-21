import pandas as pd

class UsingBureauModel:
    def __init__(self, bureau_name, bureau_code):
        self.bureau_code = bureau_code
        self.bureau_name = bureau_name

class UsingBureau:
    insert_using_bureau_query = "insert into UsingBureau (using_bureau_name, using_bureau_code) values (?,?)"
    def __init__(self, bureau_code_column, bureau_name_column, connection):
        self.bureau_name_column = bureau_name_column
        self.bureau_code_column = bureau_code_column
        self.connection = connection

    def saveDatabase(self, using_bureau_item):
        using_bureau_val = (using_bureau_item.bureau_name, int(using_bureau_item.bureau_code))
        cursor = self.connection.cursor()
        cursor.execute(self.insert_using_bureau_query, using_bureau_val)
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