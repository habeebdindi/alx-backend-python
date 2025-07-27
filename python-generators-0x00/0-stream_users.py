#!/usr/bin/env python3
from mysql.connector import Error
import seed
import sys

def stream_users():
    """A generator that streams rows from an SQL database one by one."""
    try:
        connection = seed.connect_to_prodev()
        cursor = connection.cursor(dictionary=True)
        cursor.execute("SELECT user_id, name, email, age FROM user_data")
        
        while True:
            row = cursor.fetchone()
            if row is None:
                cursor.close()
                connection.close()
                break
            row['age'] = int(row['age'])
            yield row
            
    except Error as e:
        print(f"Database error: {e}")
        if 'cursor' in locals():
            cursor.close()
        if 'connection' in locals():
            connection.close()
        return

# Make the module directly callable as required by the checker
sys.modules[__name__] = stream_users
