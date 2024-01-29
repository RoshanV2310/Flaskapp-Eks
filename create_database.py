import os
import mysql.connector

# MySQL connection parameters
db_config = {
    'host': os.environ.get('DB_HOST'),  # Align with your app.py setting
    'user': os.environ.get('DB_USERNAME'),
    'password': os.environ.get('DB_PASSWORD'),
    'database': os.environ.get('DB_NAME', 'mydb'),  # Align with your app.py setting
    'port': int(os.environ.get('DB_PORT', 3306)),
}

# Connect to MySQL
connection = mysql.connector.connect(**db_config)
cursor = connection.cursor()

# Create the 'mydb' database if it doesn't exist
cursor.execute('CREATE DATABASE IF NOT EXISTS mydb')

# Switch to 'mydb' database
cursor.execute('USE mydb')

# Create the 'messages' table if it doesn't exist
cursor.execute('''
    CREATE TABLE IF NOT EXISTS messages (
        id INT AUTO_INCREMENT PRIMARY KEY,
        message TEXT
    )
''')

# Commit and close the connection
connection.commit()
cursor.close()
connection.close()
