class RealPropertyUseModel:
    def __init__(self, name, code):
        self.name = name
        self.code = code

class RealPropertyUse:
    def createTable(self):
        cursor = self.connection.cursor()
        cursor.execute(self.create_table_sql)
        self.connection.commit()
    create_table_sql = '''        CREATE TABLE RealPropertyUses (
            real_property_use_id int primary key IDENTITY NOT NULL,
            name nvarchar(250),
            code nvarchar(250)
            );
            '''
    table_name = "RealPropertyUses"
    insert_real_property_use_query = "insert into RealPropertyUses (name, code) values (?, ?)"
    get_real_property_use_by_id = "select real_property_use_id from RealPropertyUses where name=? and code=?"
    def __init__(self, name_column, code_column, connection):
        self.name_column = name_column
        self.code_column = code_column
        self.connection = connection
        #self.createTable()

    def getRealPropertyUseId(self, name, code):    
        cursor = self.connection.cursor()
        cursor.execute(self.get_real_property_use_by_id, (name, str(code)))
        real_property_use_id = cursor.fetchone()
        if real_property_use_id is None:
            return 0
        return real_property_use_id[0]

    def saveDatabase(self, real_property_use_item):
        cursor = self.connection.cursor()
        cursor.execute(self.insert_real_property_use_query, (real_property_use_item.name, real_property_use_item.code))
        self.connection.commit()

    def separateData(self):
        real_property_use_list = []
        list_temp_2 = []
        for index in range(len(self.name_column)):
            if self.name_column[index] in list_temp_2:
                continue
            else: 
                list_temp_2.append(self.name_column[index])
                real_property_use_list.append(RealPropertyUseModel(self.name_column[index], str(self.code_column[index])))
        for real_property_use_item in real_property_use_list:
            self.saveDatabase(real_property_use_item)

    