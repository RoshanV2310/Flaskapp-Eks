from app import app, mysql

with app.app_context():
    cur = mysql.connection.cursor()
    cur.execute('CREATE DATABASE IF NOT EXISTS mydb')
    mysql.connection.commit()
    cur.close()

with app.app_context():
    cur = mysql.connection.cursor()
    cur.execute('''
        CREATE TABLE IF NOT EXISTS mydb.messages (
            id INT AUTO_INCREMENT PRIMARY KEY,
            message TEXT
        )
    ''')
    mysql.connection.commit()
    cur.close()
