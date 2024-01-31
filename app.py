# Updated app.py
import os
from flask import Flask, render_template, request, redirect, url_for
from flask_mysqldb import MySQL

app = Flask(__name__)

# Configure MySQL from environment variables
app.config['MYSQL_HOST'] = os.environ.get('DB_HOST')
app.config['MYSQL_USER'] = os.environ.get('DB_USERNAME')
app.config['MYSQL_PASSWORD'] = os.environ.get('DB_PASSWORD')
app.config['MYSQL_DB'] = os.environ.get('DB_NAME')
app.config['MYSQL_PORT'] = int(os.environ.get('DB_PORT', 3306))

# Initialize MySQL
mysql = MySQL(app)

@app.route('/')
def hello():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    first_name = request.form.get('first_name')
    last_name = request.form.get('last_name')
    new_message = request.form.get('new_message')

    cur = mysql.connection.cursor()
    cur.execute('INSERT INTO messages (first_name, last_name, message) VALUES (%s, %s, %s)',
                [first_name, last_name, new_message])
    
    mysql.connection.commit()
    cur.close()
    
    return redirect(url_for('hello'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
