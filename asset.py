class AssetModel:
    def __self__(self, asset_status, asset_status_code):
        self.asset_status = asset_status
        self.asset_status_code = asset_status_code

class Asset:
    def createTable(self):
        cursor = self.connection.cursor()
        cursor.execute(self.create_table_sql)
        self.connection.commit()

    create_table_sql = '''      CREATE TABLE Assets (
            asset_id int primary key IDENTITY NOT NULL,
            asset_status nvarchar(250),
            asset_status_code nvarchar(250)
            );
            '''
    table_name = "Assets"
    insert_asset_query = "insert into Assets (asset_status, asset_status_code) values (?, ?)"
    get_asset_by_id = "select asset_id from Assets where asset_status=? and asset_status_code=?"

    def __init__(self, asset_status_column, asset_status_code_column, connection):
        self.asset_status_column = asset_status_column
        self.asset_status_code_column = asset_status_code_column
        self.connection = connection
        #self.createTable()

    def getAssetId(self, asset_status, asset_status_code):
        cursor = self.connection.cursor()
        cursor.execute(self.get_asset_by_id, (asset_status, asset_status_code))
        asset_id = cursor.fetchone()
        return asset_id[0]

    def saveDatabase(self, asset_item):
        cursor = self.connection.cursor()
        cursor.execute(self.insert_asset_query, asset_item)
        self.connection.commit()

    def separateData(self):
        asset_list =  []
        for index in  range(len(self.asset_status_column)):
            if self.asset_status_column[index] in asset_list:
                continue
            else:
                asset_list.append(self.asset_status_column[index])
                asset_item = (str(self.asset_status_column[index]), str(self.asset_status_code_column[index]))
                self.saveDatabase(asset_item)
    