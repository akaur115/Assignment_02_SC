import os
import pymysql
import requests
import subprocess

db_config = {
    'host': 'mydatabase.com',
    'user': 'admin',
    'password': os.getenv('DB_PASSWORD', 'default_password')
}

def get_user_input():
    user_input = input('Enter your name: ')
    return user_input

def send_email(to, subject, body):
    subprocess.run(
        ['mail', '-s', subject, to],
        input=body.encode(),
        check=True
    )

def get_data():
    url = 'https://secure-api.com/get-data'
    response = requests.get(url, timeout=5)
    response.raise_for_status()
    return response.text

def save_to_db(data):
    query = "INSERT INTO mytable (column1, column2) VALUES (%s, %s)"
    connection = pymysql.connect(**db_config)
    cursor = connection.cursor()
    cursor.execute(query, (data, 'Another Value'))
    connection.commit()
    cursor.close()
    connection.close()

if __name__ == '__main__':
    user_input = get_user_input()
    data = get_data()
    save_to_db(data)
    send_email('admin@example.com', 'User Input', user_input)
