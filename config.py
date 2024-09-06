import mysql.connector

# DB 연결 설정
def get_db_config():
    return {
        'host': '192.168.0.197',
        'user': 'team3',
        'password': '123456',
        'database': 'pydb3'
    }

def connection():
    config = get_db_config()
    return mysql.connector.connect(**config)