from clickhouse_driver import Client
from common.read_config import ReadConfig
from common.project_path import conf_path

db_config = ReadConfig(conf_path).get_data("DB", "config")


class DoClickhouse:
    '''对数据库进行查询'''

    def do_clickhouse(self, query):
        '''
        查询数据库，返回数据的条数
        '''
        cnn = Client(**db_config)
        cursor = cnn.execute(query)
        l = len(cursor)
        return l

    def do_clickhouse_info(self, query):
        '''
        查询数据库，返回查询数据
        '''
        cnn = Client(**db_config)
        cursor = cnn.execute(query)

        return cursor


if __name__ == '__main__':
    pass

