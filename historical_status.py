class HistoricalStatus:
    def createTable(self):
        cursor = self.connection.cursor()
        cursor.execute(self.create_table_sql)
        self.connection.commit()

    create_table_sql = '''      CREATE TABLE HistoricalStatuses (
            historical_status_id int primary key AUTO_INCREMENT NOT NULL,
            historical_status nvarchar(250)
            );
            '''
    table_name = "HistoricalStatuses"
    insert_historical_status_query = "insert into HistoricalStatuses (historical_status) values (%s)"
    get_historical_status_by_id = "select historical_status_id from HistoricalStatuses where historical_status=%s"

    def __init__(self, historical_status_column, connection):
        self.historical_status_column = historical_status_column
        self.connection = connection
        self.createTable()

    def getHistoricalStatusId(self, historical_status):
        cursor = self.connection.cursor()
        cursor.execute(self.get_historical_status_by_id, (historical_status,))
        historical_status_id = cursor.fetchone()
        return historical_status_id[0]

    def saveDatabase(self, historical_status_item):
        cursor = self.connection.cursor()
        cursor.execute(self.insert_historical_status_query, (historical_status_item, ))
        self.connection.commit()

    def separateData(self):
        _historical_status_list = self.historical_status_column.unique()
        for index in range(len(_historical_status_list)):
            self.saveDatabase(_historical_status_list[index])