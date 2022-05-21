import pandas as pd
class StateModel:
    def __init__(self, state_code, state_name):
        self.state_name = state_name
        self.state_code = state_code

class State: 
    insert_state_query = "insert into State (state_name, state_code) values (?,?)"
    def __init__(self, state_code_column, state_name_column, connection):
        self.state_code_column = state_code_column
        self.state_name_column = state_name_column
        self.connection = connection

    def saveDatabase(self, state_item):
        cursor = self.connection.cursor()
        cursor.execute(self.insert_state_query, state_item.state_name, state_item.state_code)
        self.connection.commit()
        cursor.close()

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