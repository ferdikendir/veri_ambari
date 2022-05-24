class UtilizationModel:
    def __init__(self,
                 utilization,
                 utilization_code):
        self.utilization = utilization
        self.utilization_code = utilization_code

class Utilization:
    def createTable(self):
        cursor = self.connection.cursor()
        cursor.execute(self.create_table_sql)
        self.connection.commit()

    create_table_sql = '''      CREATE TABLE Utilizations (
            utilization_id int primary key AUTO_INCREMENT NOT NULL,
            utilization nvarchar(250),
            utilization_code nvarchar(250)
            );
            '''
    table_name = "Utilizations"
    insert_utilization_query = "insert into Utilizations (utilization, utilization_code) values (%s, %s)"
    get_utilization_by_id = "select utilization_id from Utilizations where utilization=%s and utilization_code=%s"

    def __init__(self, utilization_column, utilization_code_column, connection):
        self.utilization_column = utilization_column
        self.utilization_code_column = utilization_code_column
        self.connection = connection
        self.createTable()

    def getUtilizationId(self, utilization, utilization_code):
        cursor = self.connection.cursor()
        cursor.execute(self.get_utilization_by_id, (utilization, str(utilization_code)))
        utilization_id = cursor.fetchone()
        return utilization_id[0]

    def saveDatabase(self, utilization_item):
        cursor = self.connection.cursor()
        cursor.execute(self.insert_utilization_query, (utilization_item))
        self.connection.commit()

    def separateData(self):
        _utilization_list = []
        for index in range(len(self.utilization_column)):
            if self.utilization_column[index] in _utilization_list:
                continue
            else:
                _utilization_list.append(self.utilization_column[index])
                utilization_item = (str(self.utilization_column[index]), str(self.utilization_code_column[index]))
                self.saveDatabase(utilization_item)