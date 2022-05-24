class RealPropertyTypeModel:
    def __init__(self, real_property_code, real_property_name):
        self.real_property_code = real_property_code
        self.real_property_name = real_property_name

class RealPropertyType:
    def createTable(self):
        cursor = self.connection.cursor()
        cursor.execute(self.create_table_sql)
        self.connection.commit()

    create_table_sql = '''        CREATE TABLE RealPropertyTypes (
            real_property_type_id int primary key AUTO_INCREMENT NOT NULL,
            real_property_code nvarchar(250),
            real_property_name nvarchar(250)
            );
            '''
    table_name = "RealPropertyTypes"
    insert_real_property_type_query = "insert into RealPropertyTypes (real_property_code, real_property_name) values (%s, %s)"
    get_real_property_type_by_id = "select real_property_type_id from RealPropertyTypes where real_property_code=%s and real_property_name=%s"

    def __init__(self, real_property_code_column, real_property_name_column, connection):
        self.real_property_code_column = real_property_code_column
        self.real_property_name_column = real_property_name_column
        self.connection = connection
        self.createTable()

    def getRealPropertyTypeId(self, real_property_code, real_property_name):    
        cursor = self.connection.cursor()
        cursor.execute(self.get_real_property_type_by_id, (str(real_property_code), real_property_name))
        real_property_type_id = cursor.fetchone()
        if real_property_type_id is None:
            return 0
        return real_property_type_id[0]

    def saveDatabase(self, real_property_type_item):
        cursor = self.connection.cursor()
        cursor.execute(self.insert_real_property_type_query, real_property_type_item)
        self.connection.commit()

    def separateData(self):
        real_property_type_code_list =  self.real_property_code_column.unique()
        real_property_type_name_list =  self.real_property_name_column.unique()
        for index in  range(len(real_property_type_code_list)):
            real_property_type_item = (str(real_property_type_code_list[index]), real_property_type_name_list[index])
            self.saveDatabase(real_property_type_item)