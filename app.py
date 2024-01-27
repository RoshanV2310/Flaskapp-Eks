import os
from flask import Flask, render_template, request, redirect, url_for
from flask_mysqldb import MySQL

app = Flask(__name__)

# Configure MySQL from environment variables
app.config['MYSQL_HOST'] = os.environ.get('MYSQL_HOST')
app.config['MYSQL_USER'] = os.environ.get('MYSQL_USER')
app.config['MYSQL_PASSWORD'] = os.environ.get('MYSQL_PASSWORD')
app.config['MYSQL_DB'] = os.environ.get('MYSQL_DB')

# Initialize MySQL
mysql = MySQL(app)

# Function to initialize the database with required table
def init_db():
    with app.app_context():
        cur = mysql.connection.cursor()

        # Create the database if it doesn't exist
        cur.execute('CREATE DATABASE IF NOT EXISTS mydb;')
        cur.execute('USE mydb;')

        # Create the "messages" table if it doesn't exist
        cur.execute('''
            CREATE TABLE IF NOT EXISTS messages (
                id INT AUTO_INCREMENT PRIMARY KEY,
                message TEXT
            )
        ''')

        cur.close()
        mysql.connection.commit()

# Flask route to display and submit messages
@app.route('/', methods=['GET', 'POST'])
def hello():
    if request.method == 'POST':
        new_message = request.form.get('new_message')
        cur = mysql.connection.cursor()
        cur.execute('INSERT INTO messages (message) VALUES (%s)', [new_message])
        mysql.connection.commit()
        cur.close()

    cur = mysql.connection.cursor()
    cur.execute('SELECT message FROM messages')
    messages = cur.fetchall()
    cur.close()

    return render_template('index.html', messages=messages)

# Run database initialization and Flask app when the script is executed
if __name__ == '__main__':
    # Perform database initialization
    init_db()
    
    # Run the Flask app
    app.run(host='0.0.0.0', port=5000, debug=True)
