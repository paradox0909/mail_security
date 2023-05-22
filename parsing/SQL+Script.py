import re
import mysql.connector

# 정규표현식 패턴
pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b'
emails = []

# Apache2 로그 파일 읽기
with open('/var/log/apache2/access.log', 'r') as file:
    for line in file:
        matches = re.findall(pattern, line)
        for match in matches:
            if match not in emails:
                emails.append(match)

# MySQL 연결 설정
connect = mysql.connector.connect(
    user='tester',
    password='blaster_09',
    host='127.0.0.1',
    database='solution',
)

if connect.is_connected():
    cursor = connect.cursor()

    # 이메일을 순회하며 clicked 필드의 값을 1로 업데이트
    for email in emails:
        cursor.execute("UPDATE result SET clicked = 1 WHERE email = %s", (email,))

    connect.commit()
    connect.close()

    if not connect.is_connected():
        print("Bye")
