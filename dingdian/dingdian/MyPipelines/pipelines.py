#coding=utf-8
import pymysql        

class sql:
    '''
    insert sql
    '''
    @classmethod
    def  insert_sql():
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
        cur.execute("select supplier_name from think_supplier_list where qichacha=0 and id>20 and id<50")