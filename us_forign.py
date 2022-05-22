import pandas as pd
class USForeignModel:
    def __init__(self, us_forign_name):
        self.us_foreign_name = us_forign_name

class USForeign:
    def createTable(self):
        cursor = self.connection.cursor()
        cursor.execute(self.create_table_sql)
        self.connection.commit()

    create_table_sql = '''
            CREATE TABLE US_Foreigns (
                us_foreign_id int primary key IDENTITY(1,1) NOT FOR REPLICATION NOT NULL,
                us_foreign_name nvarchar(50)
                )
                '''
    table_name = 'USForeigns'
    insert_us_forign_query = "insert into US_Foreigns (us_foreign_name) values (?)"
    get_us_forign_by_id = "select us_foreign_id from US_Foreigns where us_foreign_name=?"

    def __init__(self, us_forign_name, connection):
        self.us_forign_name = us_forign_name
        self.connection = connection
        #self.createTable()

    def saveDatabase(self, us_foreign_item):
        us_foreign_val = (us_foreign_item.us_foreign_name)
        cursor = self.connection.cursor()
        cursor.execute(self.insert_us_forign_query, us_foreign_val)
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