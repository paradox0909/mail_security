import re
import mysql.connector

pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b'
button_pattern = r'\b\/warning\.jpg\?email\=[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b'

emails = []
button_clicked_emails = []

with open('/var/log/apache2/access.log', 'r') as file:
    for line in file:
        matches = re.findall(pattern, line)
        button_matches = re.findall(button_pattern, line)
        for match in matches:
            if match not in emails:
                emails.append(match)
        for button_match in button_matches:
            email = re.findall(r'email=([A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,})', button_match)
            if email:
                email = email[0]
                if email not in emails:
                    emails.append(email)
                    button_clicked_emails.append(email)

connect = mysql.connector.connect(
    user='tester',
    password='blaster_09',
    host='127.0.0.1',
    database='solution',
)

if connect.is_connected():
    cursor = connect.cursor()

    for email in emails:
        cursor.execute("UPDATE result SET clicked = 1 WHERE email = %s", (email,))
        if email in button_clicked_emails:
            cursor.execute("UPDATE result SET button_clicked = 1 WHERE email = %s", (email,))
        else:
            cursor.execute("UPDATE result SET button_clicked = 0 WHERE email = %s", (email,))

    connect.commit()
    connect.close()

    if not connect.is_connected():
        print("작업 완료")
