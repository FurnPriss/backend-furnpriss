from numpy import load
import pymysql, os

db = cursor = None 

class QuerySet:
    def __init__(self):
        self.user = os.environ.get("NAME")
        self.database = os.environ.get("DATABASE")
        self.password = os.environ.get("PASSWORD")
        self.host = os.environ.get("HOST")
    
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
    
    def dataGraph(self, month, user_id):
        global cursor

        self.openDB()
        cursor.execute(
            f"""
                SELECT 
                    p.category, sum(s.your_price) as revenue, s.removed_stock 
                FROM
                    price_predict_product p, price_predict_stockout s
                WHERE 
                    month(s.created_date)='{month}' AND s.product_id=p.id_product AND s.user_id=p.user_id AND s.user_id='{user_id}'
                GROUP BY p.category
                ORDER BY s.removed_stock DESC
            """
        )
        container = cursor.fetchall()
        return container

# obj = QuerySet()
# print(obj.dataGraph(4))