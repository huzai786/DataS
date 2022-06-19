# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import sqlite3


class Core1Pipeline:
    def __init__(self):
        self.create_conn()
        self.create_table()
        
    def create_conn(self):
        self.con = sqlite3.connect('czone.db')
        self.cur = self.con.cursor()
        
    def create_table(self):
        self.cur.execute('''CREATE TABLE IF NOT EXISTS products(name TEXT, detail TEXT, availability TEXT, image TEXT, specs TEXT, price TEXT)''')
        
    def process_item(self, item, spider):
        self.store_db(item)
        return item
    def store_db(self, item):
        self.cur.execute('''INSERT INTO products VALUES(?,?,?,?,?,?)''',
                                        (item['name'], item['detail'], item['availability'],
                                        item['image'], item['specs'], item['price']))
        self.con.commit()