from flask import Flask, jsonify, json, make_response, request

from appmenu import menu_blueprint  # appmenu.py에서 Blueprint 가져오기

app = Flask(__name__)

# 한글 깨짐 처리
app.config['JSON_AS_ASCII'] = False

# DB 연결 설정

@app.route('/hello')
def hello():
    print('hello')
    return 'Hello, World!'


# appmenu URL을 Blueprint로 등록
app.register_blueprint(menu_blueprint)

if __name__ == '__main__':
    # app.run(debug=True)
    app.run(host='127.0.0.1', port=5000)