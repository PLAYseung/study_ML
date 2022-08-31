# 서비스 메인코드 작성(엔트리(java;main)코드)
# 1. 모듈 가져오기

from flask import Flask,request,render_template,jsonify

# 2. 플라스크 객체 생성
app = Flask(__name__)
'''
    - __name__을 기술한 py에서 직접 실행되면 __main__으로 리턴 : 주연
    - 다른 모듈에서 이 py를 호출, 모듈가져가기등등 사용하면 파일명으로 리턴 : 조연
'''
print(__name__)

# 3. 라우팅 (서버측으로 요청이들어오면 (주소/url)을 분석해서 어떤 함수가 대응할지 처리하는것)
@app.route('/') # <- 데코레이터
def home():
    # 응답 내용 -> 이 주소를 요청한 클라이언트가 보는 화면의 재료
    # 텍스트를 입력받는 화면 준비해서 클라이언트한태 랜더링하여 제공(서버 사이드 렌더링:SSR)
    return render_template('index.html')

# POST 방식으로 url이 반응하게 허용해야함 기본은 GET 방싱
@app.route('/predict', methods=['POST'])
def predict():
    # json으로 응답, 예측행위 생략(임시)
    # 1. 클라이언트가 보낸 데이터 획득(POST 방식)
    law_text = request.form.get('key')
    print( law_text )
    # 2. 전처리 (훈련중일때는 정규식 사용이 이미 답을 알고 있어서 혼선이 없었음, 예측시에는 문제됨)
    #    입력 데이터의 최종 형태 => (1,65536), DataFrame 형태로 입력
    # 3. 모델에 입력 후 예측 수행
    # 4. 예측 결과를 받아서 응답처리
    return jsonify( {'code':1,'value':'한국어'} )

# 4. 서버가동 
if __name__=='__main__':    # 라이브러리 테스트 or 엔트리확인   # 이 코드가 엔트리 포인트가 되면 서버 가동
    app.run(debug=True)     # 코드를 수정하면 실시간 반영됨