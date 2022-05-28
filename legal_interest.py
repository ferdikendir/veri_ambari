class LegalInterestModel:
    def __init__(self, name, code):
        self.name = name
        self.code = code

class LegalInterest:
    def createTable(self):
        cursor = self.connection.cursor()
        cursor.execute(self.create_table_sql)
        self.connection.commit()

    create_table_sql = '''      CREATE TABLE LegalInterests (
            legal_interest_id int primary key IDENTITY NOT NULL,
            name nvarchar(250),
            code nvarchar(250)
            );
            '''
    table_name = "LegalInterests"
    insert_legal_interest_query = "insert into LegalInterests (name, code) values (?, ?)"
    get_legal_interest_by_id = "select legal_interest_id from LegalInterests where name=? and code=?"

    def __init__(self, name_column, code_column, connection):
        self.name_column = name_column
        self.code_column = code_column
        self.connection = connection
        #self.createTable()

    def getLegalInterestId(self, name, code):
        cursor = self.connection.cursor()
        cursor.execute(self.get_legal_interest_by_id, (name, str(code)))
        legal_interest_id = cursor.fetchone()
        return legal_interest_id[0]

    def saveDatabase(self, legal_interest_item):
        cursor = self.connection.cursor()
        cursor.execute(self.insert_legal_interest_query, legal_interest_item)
        self.connection.commit()

    def separateData(self):
        legal_interest_name_list =  self.name_column.unique()
        legal_interest_code_list =  self.code_column.unique()
        for index in  range(len(legal_interest_name_list)):
            legal_interest_item = (str(legal_interest_name_list[index]), str(legal_interest_code_list[index]))
            self.saveDatabase(legal_interest_item)