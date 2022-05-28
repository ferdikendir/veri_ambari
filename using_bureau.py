import pandas as pd
import pyodbc

class UsingBureauModel:
    def __init__(self, bureau_name, bureau_code):
        self.bureau_code = bureau_code
        self.bureau_name = bureau_name


class UsingBureau:
    create_table_sql = '''         CREATE TABLE UsingBureaus (
            bureau_id int primary key IDENTITY NOT NULL,
            bureau_code nvarchar(50),
            bureau_name nvarchar(50)
            );
            '''
    table_name = 'UsingBureaus'
    insert_bureau_query = "insert into UsingBureaus (bureau_name, bureau_code) values (?, ?)"
    get_bureau_by_id = "select bureau_id from UsingBureaus where bureau_code=? and bureau_name=?"

    def createTable(self):
        cursor = self.connection.cursor()
        cursor.execute(self.create_table_sql)
        self.connection.commit()

    def __init__(self, bureau_code_column, bureau_name_column, connection):
        self.bureau_name_column = bureau_name_column
        self.bureau_code_column = bureau_code_column
        self.connection = connection
        #self.createTable()

    def getBureauId(self, bureau_code, bureau_name):
        cursor = self.connection.cursor()
        cursor.execute(self.get_bureau_by_id, (str(bureau_code), bureau_name))
        bureau_id = cursor.fetchone()
        if bureau_id is None:
            return 0
        return bureau_id[0]

    def saveDatabase(self, using_bureau_item):
        using_bureau_val = (using_bureau_item.bureau_name, str(using_bureau_item.bureau_code))
        cursor = self.connection.cursor()
        cursor.execute(self.insert_bureau_query, using_bureau_val)
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