import seed
from mysql.connector import Error

def stream_user_ages():
    try:
        connection = seed.connect_to_prodev()
        cursor = connection.cursor(dictionary=True)
        cursor.execute("SELECT age FROM user_data")

        while True:
            row = cursor.fetchone()
            if row is None:
                cursor.close()
                connection.close()
                break
            yield row['age']
    except Error as e:
        print(f"Database error: {e}")
        return

def avg_age():
    count = 0
    total_sum = 0
    for age in stream_user_ages():
        total_sum += age
        count += 1
    avg = total_sum/count
    print(f"Average age of users: {avg}")
    return avg
