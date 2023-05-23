#Have to on the sendmail
#Smtp mail sender 
#Have to on servce sendmail start
import os                                   # os 모듈을 가져옴. 파일을 만들고, 삭제하고, 읽고, 쓰는데 사용 가능
import smtplib                              # smtplib 모듈을 가져옴. smtplib는 이메일을 보내고 받는데 사용할 수 있음. SMTP 서버에 연결 후 메시지를 송수진하는데 사용됨.
from email.mime.text import MIMEText        # email.mime.text 모듈에서 MIMEText 클래스를 가져옵니다. MIMEText 클래스는 텍스트 이메일을 만들고 보내는 데 사용됨.

with open('mail_body.txt', 'r') as f:       # mail_body.txt 파일을 읽기 모드로 연다.
    body = f.read()                         # body 라는 한수에 저장합니다.


sender = 'dokingkns2006@gmail.com'          # 보내는 사람 이메일    
recipients = open('receivers.txt', 'r')     # receivers.txt라는 텍스트 파일을 읽기 모드로 열고 파일 객체를 변수 recipients에 할당하여 파일의 내용에 접근하고 읽을 수 있게 합니다.
recipient= recipients.readline()            # readlone() 메서드를 사용하여 파일 객체 recipients에서 한 줄을 읽습니다.
                                            # 그 줄의 내용을 변수 recipient에 할당함. 첫 번째 줄을 읽어 recipient 변수에 저장함.

while recipient :                           # recipient 변수가 존재하는 한 계속해서 반복하는 반복문입니다. recipient 변수에 값이 할당되어 있는 한 반복문의 내용이 실행됩니다. 
    changebody = body.replace('tempmail',recipient) # 문자열 body에서 tempmail이라는 부분을 recipient 변수로 대체하여 changebody 변수에 할당함. 즉, body 문자열에서 tempmail 부분을  recipient 값으로 바꾼 새로운 문자열을 생성합니다. 
    msg = MIMEText(changebody,"html")       # changebody 값을 이용하여 MINEText 객체를 생성하고 HTML 형식의 텍스트로 이 객체를 생성합니다. 이메일의 본문에 해당됩니다.   
    msg['Subject'] = 'title'                # 이메일의 제목 설정    
    msg['From'] = sender                    # 이메일을 보내는 사람의 주소
    msg['To'] = recipient                   # msg 메시지 객체의 'To' 필드에 recipient 값을 할당합니다. 이메일의 수신자 주소를 절정하는 부분입니다.

    try:
        smtpObj = smtplib.SMTP('localhost') # localhost를 이용하여 smtplib.SMTP 객체를 생성 및 smtpObj 변수에 할당함 . SMTP 서버와의 연결을 나타냅니다.
        smtpObj.sendmail(sender, recipient, msg.as_string()) # smtp 객체의 sendmail 메서드를 호출하여 이메일을 보냄. msg.as_string은 이메일 메시지를 문자열 형식으로 나타낸 것입니다.
        print("Email sent successfully.")   # print 이메일이 성공적으로 전송되었습니다. 
        recipient= recipients.readline()    # recipients 파일 객체에서 다음 줄을 읽어 recipient 변수에 할당합니다. 이는 다음 수신자의 이메일 주소를 가져오는 부분입니다.
    except Exception as e:                  # 예외가 발생한 경우 해당 예외를 잡고 처리하기 위한 예외 처리 블록의 시작. Exception 클래스는 모든 예외의 기본 클래스이며, as e는 예외 객체를 변수 'e'에 할당하는것을 의미합니다.
        print("error has occurred.", e)     # 예외가 발생한 경우 해당 예외와 함께 error has occurred 라는 메시지를 출렵합니다. 이는 예외 처리 블록에서 예외가 발생했을때 실행됩니다. 'e' 변수는 발생한 예외를 나타냅니다.
