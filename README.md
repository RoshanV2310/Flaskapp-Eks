Flask App with MySQL Docker Setup
This is a simple Flask app that interacts with a MySQL database. The app allows users to submit messages, which are then stored in the database

DataBase

CREATE SCHEMA IF NOT EXISTS mydb;

use mydb;

CREATE TABLE IF NOT EXISTS messages (id INT AUTO_INCREMENT PRIMARY KEY,first_name VARCHAR(255) NOT NULL,last_name VARCHAR(255) NOT NULL,message TEXT NOT NULL);

SHOW TABLES;

SELECT * FROM messages;
