# mail_security
Hello I am Paradox who creator of this program.
Please do not abuse it and only use it to strengthen your company's security.

##### Recommand Operating System is Ubuntu latest Version
```
$ apt update
$ apt install apache2 mysql python3 smtp vim pip3 -y
$ pip3 update
$ pip3 install smtplib mysql-connector-python -y
```

<pre><code>$ git clone https://github.com/paradox0909/mail_security.git</code></pre>
<pre><code>$ cd mail_security</code></pre>

##### setting a receivers and mail_body
##### change directory to mail_security/send_mail
<pre><code>$ cd mail_security/send_mail</code></pre>
##### edit a receivers.txt
##### (please enter one email and add a line break)

##### you can send email to html.
##### if you change a mail body, add a 
```
<img src="http://127.0.0.1/test.png?email='test_parameter'"> 
```
##### this code will you can determine whether an email has been read based on whether the photo has been read.
