#!/usr/bin/env python3
from mysql.connector import Error
import sys

def stream_users_in_batches(batch_size):
    try:
        connection = __import__('seed').connect_to_prodev()
        cursor = connection.cursor(dictionary=True)
        cursor.execute("SELECT user_id, name, email, CAST(age AS SIGNED) as age FROM user_data")

        while True:
            batch = cursor.fetchmany(batch_size)
            if not batch:
                cursor.close()
                connection.close()
                break
            yield batch
    except Error as e:
        print(f"Database error: {e}")
        if 'cursor' in locals():
            cursor.close()
        if 'connection' in locals():
            connection.close()
        return

def batch_processing(batch_size):
    try:
        for batch in stream_users_in_batches(batch_size):
            for user in batch:
                print(user)
    except Exception as e:
        print(f"Processing error: {e}")
        return
