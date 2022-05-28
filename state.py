import pandas as pd
import pyodbc
class StateModel:
    def __init__(self, state_code, state_name):
        self.state_name = state_name
        self.state_code = state_code

class State:
    def createTable(self):
        cursor = self.connection.cursor()
        cursor.execute(self.create_table_sql)
        self.connection.commit()
    create_table_sql = '''            CREATE TABLE States (
                state_id int primary key IDENTITY NOT NULL,
                state_name nvarchar(50),
                state_code nvarchar(50)
                );
                '''
    table_name = 'States'
    insert_state_query = "insert into States (state_name, state_code) values (?, ?)"
    get_state_by_id = "select state_id from States where state_name=? and state_code=?"


    def __init__(self, state_code_column, state_name_column, connection):
        self.state_code_column = state_code_column
        self.state_name_column = state_name_column
        self.connection = connection
        #self.createTable()

    def getStateId(self, state_name, state_code):
        cursor = self.connection.cursor()
        cursor.execute(self.get_state_by_id, (state_name, str(state_code)))
        row = cursor.fetchone()
        if row is None:
            return 0
        return row[0]

    def saveDatabase(self, state_item):
        state_val = (state_item.state_name, str(state_item.state_code))
        cursor = self.connection.cursor()
        cursor.execute(self.insert_state_query, state_val)
        self.connection.commit()

    def separateData(self):
        state_list = []
        list_temp_5 = []
        for index in range(len(self.state_name_column)):
            if self.state_name_column[index] in list_temp_5:
                continue
            else: 
                list_temp_5.append(self.state_name_column[index])
                state_list.append(StateModel(self.state_code_column[index], self.state_name_column[index]))
        for state_item in state_list:
            if(pd.isna(state_item.state_name)):
                state_item.state_name = "null"

            if(pd.isna(state_item.state_code)):
                state_item.state_code = 0
            self.saveDatabase(state_item)