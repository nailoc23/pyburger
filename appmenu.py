from flask import Blueprint

# Blueprint 생성
menu_blueprint = Blueprint('appmenu', __name__)

# 새로운 memu 목록
@menu_blueprint.route('/menulist')
def menulist():

    res = "{'test'; '1234'}"
    return res