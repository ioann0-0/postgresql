import psycopg2
from psycopg2 import sql

conn = psycopg2.connect(
    dbname='my_database',
    user='your_user',
    password='your_password',
    host='localhost'
)
conn.autocommit = False
cur = conn.cursor()

def create_record(name, age):
    try:
        cur.execute("INSERT INTO my_table (name, age) VALUES (%s, %s)", (name, age))
        conn.commit()
    except Exception as e:
        conn.rollback()
        print(f"Error: {e}")

def read_all_records():
    cur.execute("SELECT * FROM my_table")
    rows = cur.fetchall()
    for row in rows:
        print(row)

def read_record(record_id):
    cur.execute("SELECT * FROM my_table WHERE id = %s", (record_id,))
    row = cur.fetchone()
    print(row)

def update_record(record_id, name, age):
    try:
        cur.execute("UPDATE my_table SET name = %s, age = %s WHERE id = %s", (name, age, record_id))
        conn.commit()
    except Exception as e:
        conn.rollback()
        print(f"Error: {e}")

def delete_record(record_id):
    try:
        cur.execute("DELETE FROM my_table WHERE id = %s", (record_id,))
        conn.commit()
    except Exception as e:
        conn.rollback()
        print(f"Error: {e}")

def close_connection():
    cur.close()
    conn.close()

if __name__ == "__main__":
    create_record('Alice', 30)
    create_record('Bob', 25)
    read_all_records()
    read_record(1)
    update_record(1, 'Alicia', 31)
    read_record(1)
    delete_record(2)
    read_all_records()
    close_connection()
