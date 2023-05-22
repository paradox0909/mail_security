import re
import mysql.connector

# 정규표현식 패턴
pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b' # pattern이라는 변수에 정규 표현식 패턴을 할당.
# 이메일 변수 저장
emails = []            # emails라는 빈 목록을 만듬. Apache2 로그 파일에서 발견된 모든 이메일 주소가 저장됩니다.

# Apache2 로그 파일 읽기
with open('/var/log/apache2/access.log', 'r') as file:        # /var/log/apach2/access.log 경로로 가서 apache2 access.log 파일을 가져옴   
    for line in file:                                         # 파일의 각 줄에 대해 반복합니다.  
        matches = re.findall(pattern, line)                   # re.findall() 함수를 사용해서 줄에서 이메일 주소를 찾음.
        for match in matches:               # matches 목록에 있는 각 이메일 주소에 대해 반복. matches 목록은 re.findall() 함수를 사용하여 로그 파일의 각 줄에서 찾은 이메일 주소를 저장.   
            if match not in emails:         # 이메일 주소가 emails 목록에 없으면 목록에 추가합니다.                  
                emails.append(match)        # 파일을 닫습니다.

# MySQL 연결 설정
connect = mysql.connector.connect(                              # connect 라는 변수를 생성하고 그 변수에 MySQL 연결 설정을 해줌.
    user='tester',                                              
    password='blaster_09',
    host='127.0.0.1',
    database='solution',
)

if connect.is_connected():                                      # 만약 mysql에 연결된다면
    cursor = connect.cursor()                                   # 커서라는 변수를 만들고 커서에 연결.

    # 이메일을 순회하며 clicked 필드의 값을 1로 업데이트
    for email in emails:                                        # email 목록에 있는 각 이메일 주소에 대해 반복합니다.
        cursor.execute("UPDATE result SET clicked = 1 WHERE email = %s", (email,))
        # result라는 테이블에서 이메일 주소와 일치하는 행을 업데이트하고 clicked 열의 값을 1로 설정합니다.
    connect.commit() # 커서가 변경한 모든 데이터베이스 변경사항을 커밋합니다.
    connect.close()  # 연결을 닫습니다

    if not connect.is_connected():           # 만약 connect 되어있지 않으면 
        print("Bye")
