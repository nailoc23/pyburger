from flask import Blueprint, jsonify, json, make_response, request
from model import MenuModel  # model.py에서 EmployeeModel 클래스 가져오기

# Blueprint 생성
menu_blueprint = Blueprint('appmenu', __name__)

# DB 연결 설정
db_config = {
    'host': '192.168.0.197',
    'user': 'team3',
    'password': '123456',
    'database': 'pydb3'
}

# 새로운 memu 목록
@menu_blueprint.route('/menu')
def menu():

    res = "{'test'; '1234'}"
    return res

@menu_blueprint.route('/menulist')
def menulist():
    # MenuModel 인스턴스 생성
    menu_model =  MenuModel(db_config)

    # 메뉴 데이터 가져오기
    data = menu_model.get_all_menus()

    # JSON 응답 생성
    data = json.dumps(data, ensure_ascii=False)
    res = make_response(data)
    
    return res