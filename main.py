import first
import send

def setting(authorize_code):
    first.first_kakao(authorize_code) #파라미터 값 : authorize_code(정수)

def massage(index, text):
    send.send_massage(index,text) #파라미터 값 : 친구의 index(정수) , 보낼 문자 (문자열)
