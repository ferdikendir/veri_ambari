import pandas as pd
class USForeignModel:
    def __init__(self, us_forign_name):
        self.us_foreign_name = us_forign_name

class USForeign:
    insert_us_foreign_query = "insert into USForeign (us_foreign_name) values (?)"
    def __init__(self, us_forign_name, connection):
        self.us_forign_name = us_forign_name
        self.connection = connection

    def saveDatabase(self, us_foreign_item):
        cursor = self.connection.cursor()
        us_foreign_val = (us_foreign_item.us_foreign_name)
        cursor.execute(self.insert_us_foreign_query, us_foreign_val)
        self.connection.commit()
    def separateData(self):
        us_foreign_list = []
        us_foreign_names = self.us_forign_name.unique()
        for i in range(len(us_foreign_names)):
            us_foreign_list.append(USForeignModel(us_foreign_names[i]))

        for us_foreign_item in us_foreign_list:
            if(pd.isna(us_foreign_item)):
                us_foreign_item = "null"
            self.saveDatabase(us_foreign_item)