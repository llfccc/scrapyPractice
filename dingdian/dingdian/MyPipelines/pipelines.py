#coding=utf-8
import pymysql        

class sql:
    '''
    insert sql
    '''
    @classmethod
    def  insert_sql(self,name):
        '''
        no
        '''
        conn = pymysql.connect(
            host='127.0.0.1',
            port=3306,
            user='root',
            passwd='root',
            db='test',
            charset='utf8'
        )
        cur = conn.cursor()
        cur.execute("insert into nameTable  values('%s'),name")
        conn.commit()
        conn.close()

from dingdian.items import DingdianItem

class DingDianPipe(object):
    def  process_item(self,item,spider):
        name=item['name']
        sql.insert_sql(name)