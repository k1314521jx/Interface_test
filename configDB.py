import pymysql
import readConfig as readConfig
# from common.Log import MyLog as Log

localReadConfig = readConfig.ReadConfig()


class MyDB(object):
    global host, username, password, port, database, config
    host = localReadConfig.get_db("host")
    print(host)
    username = localReadConfig.get_db("username")
    print(username)
    password = localReadConfig.get_db("password")
    print(password)
    port = localReadConfig.get_db("port")
    print(port)
    database = localReadConfig.get_db("database")
    print(database)
    config = {
        'host': str(host),
        'user': username,
        'passwd': password,
        'port': int(port),
        'db': database
    }

    def __init__(self):
        # self.log = Log.get_log()
        # self.logger = self.log.get_logger()
        self.db = None
        self.cursor = None
        
    def __del__(self):#构析方法
        print('close')
        self.db.close()

    def connectDB(self):
        """
        connect to database
        :return:
        """
        try:
            # connect to DB
            self.db = pymysql.connect(**config)
            # create cursor
            self.cursor = self.db.cursor()
            print("Connect DB successfully!")
        except ConnectionError as ex:
            print('Connect DB fail')
            # self.logger.error(str(ex))

    def executeSQL(self, sql, params):
        """
        execute sql
        :param sql:
        :return:
        """
        self.connectDB()
        # executing sql
        self.cursor.execute(sql, params)
        # executing by committing to DB
        self.db.commit()
        return self.cursor

    def get_all(self, cursor):
        """
        get all result after execute sql
        :param cursor:
        :return:
        """
        value = cursor.fetchall()
        return value

    def get_one(self, cursor):
        """
        get one result after execute sql
        :param cursor:
        :return:
        """
        value = cursor.fetchone()
        return value

    # def closeDB(self):
        # """
        # close database
        # :return:
        # """
        # self.db.close()
        # print("Database closed!")

connect_DB = MyDB()
connect_DB.connectDB()