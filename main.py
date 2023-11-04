# conda install -c conda-forge fastapi uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# FastAPI 애플리케이션 생성
app = FastAPI()

# No 'Access-Control-Allow-Origin'
# CORS (Cross-Origin Resource Sharing) 설정: 다른 웹사이트에서 이 애플리케이션으로 요청을 보낼 수 있도록 허용
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],   # 모든 웹사이트에서 요청 허용 (실제 운영 환경에서는 더 제한적으로 설정해야 함)
    allow_methods=["*"],   # 모든 HTTP 메서드 허용 
    allow_headers=["*"],   # 모든 HTTP 헤더 허용
)

# '/images' 엔드포인트에 'resources' 디렉토리를 연결하는 설정
from fastapi.staticfiles import StaticFiles
app.mount("/images", StaticFiles(directory="resources"), name="images") 

# 기본 경로('/')로 들어왔을 때 실행되는 함수
@app.get("/")
async def root():
    return {"message": "Hello World"}

import pickle

# /api_v1/mlmodelwithregression with dict params
# method : post
# {
#     "texture_mean": 18.5,
#     "perimeter_mean": 102.1
# }

# '/api_v1/mlmodelwithregression' 엔드포인트에 POST 요청을 처리하는 함수
# 이 함수는 주어진 데이터를 사용하여 선형 회귀 모델로 예측을 수행합니다.
@app.post('/api_v1/mlmodelwithregression') 
def mlmodelwithregression(data:dict) :# JSON 형태의 데이터를 받음
    print('data with dict {}'.format(data))
    # data dict to 변수 활당
    texture_mean = float(data['texture_mean'])
    perimeter_mean = float(data['perimeter_mean'])

    # pkl 파일 존재 확인 코드 필요

    result_predict = 0;
    # 학습 모델 불러와 예측
    with open('datasets/BreastCancerWisconsin_Regression.pkl', 'rb') as regression_file:
        loaded_model = pickle.load(regression_file)
        input_labels = [[texture_mean, perimeter_mean]] # 학습했던 설명변수 형식 맞게 적용
        result_predict = loaded_model.predict(input_labels)
        print('Predict radius_mean Result : {}'.format(result_predict))
        pass

    # 예측값 리턴
    result = {'radius_mean':result_predict[0]}
    return result
