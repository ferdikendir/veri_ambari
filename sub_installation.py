class SubInstallationModel:
    def __init__(self, sub_installation_code):
        self.sub_installation_code = sub_installation_code

class SubInstallation:
    def createTable(self):
        cursor = self.connection.cursor()
        cursor.execute(self.create_table_sql)
        self.connection.commit()

    create_table_sql = '''        CREATE TABLE SubInstallations (
            sub_installation_id int primary key AUTO_INCREMENT NOT NULL,
            sub_installation_code nvarchar(50)
            );
            '''
    table_name = "SubInstallations"
    insert_sub_installation_query = "insert into SubInstallations (sub_installation_code) values (%s)"
    get_sub_installation_by_id = "select sub_installation_id from SubInstallations where sub_installation_code=%s"

    def __init__(self, sub_installation_code_column, connection):
        self.sub_installation_code_column = sub_installation_code_column
        self.connection = connection
        self.createTable()

    def getSubInstallationId(self, sub_installation):
        cursor = self.connection.cursor()
        cursor.execute(self.get_sub_installation_by_id, (str(sub_installation), ))
        sub_installation_id = cursor.fetchone()
        if sub_installation_id is None:
            return 1
        return sub_installation_id[0]

    def saveDatabase(self, sub_installation_item):
        cursor = self.connection.cursor()
        cursor.execute(self.insert_sub_installation_query, (str(sub_installation_item), ))
        self.connection.commit()

    def separateData(self):
        sub_installation_list = []
        list_temp_4 = []
        for index in range(len(self.sub_installation_code_column)):
            if [self.sub_installation_code_column[index]] in list_temp_4:
                continue
            else:
                sub_installation_list.append(SubInstallationModel(self.sub_installation_code_column[index]))
                list_temp_4.append([self.sub_installation_code_column[index]])
        for sub_installation_item in sub_installation_list:
            self.saveDatabase(sub_installation_item.sub_installation_code)