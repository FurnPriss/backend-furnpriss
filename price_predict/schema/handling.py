import pymysql, os
from django.conf import settings

db = cursor = None 

class QuerySet:
    def __init__(self):
        self.user = "root"
        self.database = "trvStore"
        self.password = ""
        self.host = "localhost"
    
    def openDB(self):
        global db, cursor
        db = pymysql.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database,
            )
        cursor = db.cursor(pymysql.cursors.DictCursor)
    
    def closeDB(self):
        global db, cursor 
        db.close()
    
    def dataGraph(self, month):
        global cursor

        self.openDB()
        cursor.execute(
            f"""
                SELECT 
                    p.category, sum(s.your_price) as revenue, s.removed_stock 
                FROM
                    price_predict_product p, price_predict_stockout s
                WHERE month(s.created_date)='{month}' AND s.product_id=p.id_product
                GROUP BY p.category
                ORDER BY s.removed_stock DESC
            """
        )
        container = cursor.fetchall()
        return container

# obj = QuerySet()
# print(obj.dataGraph(4))