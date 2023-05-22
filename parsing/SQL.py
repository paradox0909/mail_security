import mysql.connector

connect = mysql.connector.connect(
    user='tester',
    password='blaster_09',
    host='127.0.0.1',
    database='solution',
)

if connect.is_connected():
    db_info = connect.get_server_info()
    print('MySQL Version:', db_info)
    
    cursor = connect.cursor()

    with open('emails.txt', 'r') as file:
        for line in file:
            email = line.strip()
            cursor.execute("UPDATE result SET clicked = 1 WHERE email = %s", (email,))
    connect.commit()

 
    connect.close()

    if not connect.is_connected():
        print("Bye")
