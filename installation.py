class InstallationModel:
    def __init__(self, installation_code, installation_name): 
        self.installation_code = installation_code 
        self.installation_name = installation_name


class Installation:
    def createTable(self):
        cursor = self.connection.cursor()
        cursor.execute(self.create_table_sql)
        self.connection.commit()

    create_table_sql = '''        CREATE TABLE Installations (
            installation_id int primary key AUTO_INCREMENT NOT NULL,
            installation_name nvarchar(250),
            installation_code nvarchar(250)
            );
            '''
    table_name = "Installations"
    insert_installation_query = "insert into Installations (installation_name, installation_code) values (%s, %s)"
    get_installation_by_id = "select installation_id from Installations where installation_code=%s and installation_name=%s"

    def __init__(self, installation_code_column, installation_name_column, connection):
        self.installation_code_column = installation_code_column 
        self.installation_name_column = installation_name_column
        self.connection = connection
        self.createTable()

    def getInstallationId(self, installation_code, installation_name):
        cursor = self.connection.cursor()
        cursor.execute(self.get_installation_by_id, (installation_name, f'{installation_code}'))
        installation_id = cursor.fetchone()
        if installation_id is None:
            return 0
        return installation_id[0]

    def saveDatabase(self, name, code):
        cursor = self.connection.cursor()
        cursor.execute(self.insert_installation_query, (name, str(code)))
        self.connection.commit()

    def separateData(self):
        installation_list = []
        list = []
        for index in range(len(self.installation_name_column)):
            if self.installation_code_column[index] in list:
                continue
            else: 
                list.append(self.installation_code_column[index])
                self.saveDatabase(self.installation_name_column[index], self.installation_code_column[index])
                #installation_list.append(InstallationModel(self.installation_code_column[index], self.installation_name_column[index]))
        #for installation_item in installation_list:
            #print(installation_item.installation_code)
            #self.saveDatabase(installation_item)