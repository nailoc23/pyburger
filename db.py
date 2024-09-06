# db.py

import mysql.connector

class DBConnection:
    def __init__(self, host, user, password, database):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.connection = None
        self.cursor = None

    def connect(self):
        # 데이터베이스 연결
        self.connection = mysql.connector.connect(
            host=self.host,
            user=self.user,
            password=self.password,
            database=self.database
        )
        self.cursor = self.connection.cursor()
        return self.cursor

    def close(self):
        # 리소스 정리
        if self.cursor:
            self.cursor.close()
        if self.connection:
            self.connection.close()
