# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.conf import settings

from pymongo import MongoClient
import json


class SunPipeline(object):

    def open_spider(self, item):
        """配置数据库的连接信息, 初始化数据的连接"""

        host = settings.get('MONGO_HOST')
        port = settings.get('MONGO_PORT')
        db_name = settings.get('MONGO_DBNAME')
        col_name = settings.get('MONGO_COLNAME')
        # 连接数据库
        self.client = MongoClient(host=host, port=port)
        # 设置连接数据库的名称
        self.db = self.client[db_name]
        self.col = self.db[col_name]




    def process_item(self, item, spider):
        """讲数据写入数据库"""
        # 首先，讲字典转化为json
        dict_data = dict(item)
        # 插入数据库
        self.client.insert(dict_data)
        return item

    def close_spider(self, item):
        """关闭数据库"""
        self.client.close()
        pass



