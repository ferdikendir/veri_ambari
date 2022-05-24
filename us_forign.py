import pandas as pd
class USForeignModel:
    def __init__(self, us_forign_name):
        self.us_foreign_name = us_forign_name

class USForeign:
    def createTable(self):
        cursor = self.connection.cursor()
        cursor.execute(self.create_table_sql)
        self.connection.commit()

    create_table_sql = '''          CREATE TABLE US_Foreigns (
                us_foreign_id int primary key AUTO_INCREMENT NOT NULL,
                us_foreign_name nvarchar(50)
                );
                '''
    table_name = 'USForeigns'
    insert_us_forign_query = "insert into US_Foreigns (us_foreign_name) values (%s)"
    get_us_forign_by_id = "select us_foreign_id from US_Foreigns where us_foreign_name=%s"

    def __init__(self, us_forign_name, connection):
        self.us_forign_name = us_forign_name
        self.connection = connection
        self.createTable()

    def getUSForeignId(self, us_foreign_name):
        cursor = self.connection.cursor()
        cursor.execute(self.get_us_forign_by_id, (us_foreign_name,))
        us_foreign_id = cursor.fetchone()
        if us_foreign_id is None:
            return 0
        return us_foreign_id[0]

    def saveDatabase(self, us_foreign_name):
        cursor = self.connection.cursor()
        cursor.execute(self.insert_us_forign_query, (str(us_foreign_name), ))
        self.connection.commit()

    def separateData(self):
        us_foreign_list = []
        us_foreign_names = self.us_forign_name.unique()
        for i in range(len(us_foreign_names)):
            if(pd.isna(us_foreign_names[i])):
                us_foreign_names[i] = "null"
            self.saveDatabase(us_foreign_names[i])