from flask import Flask, jsonify, json, make_response, request

from appmenu import menu_blueprint  # appmenu.py에서 Blueprint 가져오기

import pandas as pd

app = Flask(__name__)

# 한글 깨짐 처리
app.config['JSON_AS_ASCII'] = False

# DB 연결 설정

@app.route('/hello')
def hello():
    print('hello')
    return 'Hello, World!'


@app.route('/api/endpoint', methods=['GET'])
def api_example():
    return {"message": "Hello Order from Python!"}

# CSV 파일을 판다스로 읽기
def load_data():
    # 'sales_data.csv' 파일에서 날짜와 일일 판매량 데이터를 읽어옵니다
    df = pd.read_csv('daily_sales_data.csv')
    # 예시로 컬럼이 'date'와 'sales'로 되어 있다고 가정
    labellist = df['date'].tolist()  # 날짜 데이터를 리스트로 변환
    datalist = df['sales'].tolist()  # 판매량 데이터를 리스트로 변환
    
    return labellist, datalist

def load_monthdata():
    # 'sales_data.csv' 파일에서 날짜와 일일 판매량 데이터를 읽어옵니다
    df = pd.read_csv('monthly_sales_data.csv')
    # 예시로 컬럼이 'date'와 'sales'로 되어 있다고 가정
    labellist = df['month'].tolist()  # 날짜 데이터를 리스트로 변환
    datalist = df['sales'].tolist()  # 판매량 데이터를 리스트로 변환
    
    return labellist, datalist

def load_menudata():
    # 'sales_data.csv' 파일에서 날짜와 일일 판매량 데이터를 읽어옵니다
    df = pd.read_csv('menu_sales_data.csv')
    # 예시로 컬럼이 'date'와 'sales'로 되어 있다고 가정
    labellist = df['menu'].tolist()  # 날짜 데이터를 리스트로 변환
    datalist = df['sales'].tolist()  # 판매량 데이터를 리스트로 변환
    
    return labellist, datalist

@app.route('/api/endpointlist', methods=['GET'])
def api_examplelist():

    labellist, datalist = load_data()

    print(labellist[0])

    response =  jsonify(
        {
        "labellist": [{"label": date} for date in labellist],
            # {"label": "Mar 1"},
            # {"label": "Mar 2"},
            # {"label": "Mar 3"},
            # {"label": "Mar 4"}
        "datalist": [{"data": sale} for sale in datalist]
            # {"data": 10000},
            # {"data": 25000},
            # {"data": 13000},
            # {"data": 30000}
        }
    )

    # 캐시 방지 헤더 추가
    response.headers['Cache-Control'] = 'no-store, no-cache, must-revalidate, max-age=0'
    return response

@app.route('/api/endpointmonthlist', methods=['GET'])
def api_examplemonthlist():

    labellist, datalist = load_monthdata()

    print(labellist[0])

    response =  jsonify(
        {
        "labellist": [{"label": month} for month in labellist],
            # "labellist": [{"label": "01"},
            # {"label": "02"},
            # {"label": "03"},
            # {"label": "04"}],
        "datalist": [{"data": sale} for sale in datalist]
            # "datalist" : [{"data": 4215},
            # {"data": 5312},
            # {"data": 6251},
            # {"data": 7841} ]
        }
    )

    # 캐시 방지 헤더 추가
    response.headers['Cache-Control'] = 'no-store, no-cache, must-revalidate, max-age=0'
    return response

@app.route('/api/endpointmenulist', methods=['GET'])
def api_examplemenulist():

    labellist, datalist = load_menudata()

    print(labellist[0])

    response =  jsonify(
        {
        "labellist": [{"label": menu} for menu in labellist],
            # "labellist": [{"label": "01"},
            # {"label": "02"},
            # {"label": "03"},
            # {"label": "04"}],
        "datalist": [{"data": sale} for sale in datalist]
            # "datalist" : [{"data": 4215},
            # {"data": 5312},
            # {"data": 6251},
            # {"data": 7841} ]
        }
    )

    # 캐시 방지 헤더 추가
    response.headers['Cache-Control'] = 'no-store, no-cache, must-revalidate, max-age=0'
    return response

# appmenu URL을 Blueprint로 등록
app.register_blueprint(menu_blueprint)

if __name__ == '__main__':
    app.run(debug=True)
    app.run(host='127.0.0.1', port=5000)