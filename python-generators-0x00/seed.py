#!/usr/bin/env python3
import mysql.connector
from mysql.connector import Error
import csv

def connect_db():
    """connects to the mysql database server"""
    try:
        connection = mysql.connector.connect(
                host="localhost",
                user="habeebdindi",
                password="khalEXX001"
        )
        if connection.is_connected():
            #print("connected to mysql!")
            return connection
        else:
            raise Exception("failed to connect!")
    except Error as e:
        print(f"Error creating connection: {e}")
        return

def create_database(connection):
    """creates the database ALX_prodev if it does not exist"""
    try:
        if not connection:
            raise Exception
        cursor = connection.cursor()
        cursor.execute(
            "CREATE DATABASE IF NOT EXISTS ALX_prodev"
        )
    except Error as e:
        print(f"Error creating database: {e}")
        return
    
def connect_to_prodev():
    """connects the the ALX_prodev database in MYSQL"""
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="habeebdindi",
            password="khalEXX001",
            database="ALX_prodev"
        )
        if connection.is_connected():
            #print("connected to mysql database ALX_prodev!")
            return connection
        else:
            raise Exception("failed to connect to  ALX_prodev!")
    except Error as e:
        print(f"Error creating connection: {e}")
        return

def create_table(connection):
    """creates a table user_data if it does not exists with the required fields"""
    try:
        cursor = connection.cursor()
        cursor.execute(
            "CREATE TABLE IF NOT EXISTS `user_data` ("
            " `user_id` CHAR(36) PRIMARY KEY DEFAULT (UUID()),"
            " `name` VARCHAR(255) NOT NULL,"
            " `email` VARCHAR(255) NOT NULL,"
            " `age` INTEGER NOT NULL,"
            " INDEX idx_user_id (`user_id`)"
            ") ENGINE=InnoDB;"
        )
        #print("table user_data created successfully")
    except Error as e:
        print(f"Error creating table: {e}")
        return
    
def insert_data(connection, data):
    """inserts data in the database if it does not exist"""
    try:
        cursor = connection.cursor()
        with open(data, 'r', newline='') as f:
            reader = csv.DictReader(f)
            for row in reader:
                cursor.execute(
                    f"INSERT IGNORE INTO user_data (name, email, age) VALUES (%s, %s, %s)", (row['name'], row['email'], row['age'])
                )
                connection.commit()
#                print(f"inserted {row} suuccessfully!")
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found")
        return
    except Error as e:
        print(f"Error streaming data: {e}")
        return
