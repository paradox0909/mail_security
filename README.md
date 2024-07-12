# mail_security
##### Hello I am Paradox who creator of this program.
##### Please do not abuse it and only use it to strengthen your company's security.

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

##### Now you can send email to html using receivers.txt
##### if you change a mail body, add a this code at the last line :
```
<img src="http://127.0.0.1/test.png?email='test_parameter'"> 
```
##### this code will you can determine whether an email has been read based on whether the photo has been read.


<pre><code>$ cd .. </code></pre>
<pre><code>$ cd parsing</code></pre>
##### Please Setting a Mysql settings(port,passwd etc) at SQL+Script.py.

##### Mysql Setting
```
$ CREATE DATABASE example_db;
$ USE example_db;
```

```
CREATE TABLE result (
    id INT AUTO_INCREMENT PRIMARY KEY,
    email VARCHAR(255) NOT NULL,
    clicked VARCHAR(255) NOT NULL,
    button_clicked VARCHAR(255) NOT NULL,
);
```
##### now you can see a statistics at the mysql
##### 1 means that you clicked the button in the email.
##### 0 means not readed the email or press the button. 
