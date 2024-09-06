
import mysql.connector
from db import DBConnection

class MenuModel:
    def __init__(self, db_config):
        self.db = DBConnection(**db_config)

    # 데이터 목록 가져오기
    def get_all_menus(self):
        # 데이터베이스 연결
        cursor = self.db.connect()
        
        # 쿼리 실행
        query = 'SELECT * FROM menu'
        cursor.execute(query)
        
        # 결과 가져오기
        data = cursor.fetchall()
        
        # 데이터베이스 연결 종료
        self.db.close()

        return data