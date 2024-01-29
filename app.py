import os
from flask import Flask, render_template, request, redirect, url_for
from flask_mysqldb import MySQL

app = Flask(__name__)

# Configure MySQL from environment variables
app.config['MYSQL_HOST'] = os.environ.get('DB_HOST')
app.config['MYSQL_USER'] = os.environ.get('DB_USERNAME')
app.config['MYSQL_PASSWORD'] = os.environ.get('DB_PASSWORD')
app.config['MYSQL_DB'] = os.environ.get('DB_NAME', 'mydb')  # Default to 'mydb'
app.config['MYSQL_PORT'] = int(os.environ.get('DB_PORT', 3306))

# Initialize MySQL
mysql = MySQL(app)

# Create the mydb database if it doesn't exist
with app.app_context():
    cur = mysql.connection.cursor()
    cur.execute('CREATE DATABASE IF NOT EXISTS mydb')
    mysql.connection.commit()
    cur.close()

# Create the messages table if it doesn't exist
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

@app.route('/')
def hello():
    cur = mysql.connection.cursor()
    cur.execute('SELECT message FROM mydb.messages')
    messages = cur.fetchall()
    cur.close()
    return render_template('index.html', messages=messages)

@app.route('/submit', methods=['POST'])
def submit():
    new_message = request.form.get('new_message')
    cur = mysql.connection.cursor()
    cur.execute('INSERT INTO mydb.messages (message) VALUES (%s)', [new_message])
    mysql.connection.commit()
    cur.close()
    return redirect(url_for('hello'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
