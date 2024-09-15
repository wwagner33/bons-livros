# app.py

from flask import Flask
import psycopg2
from config import Config

app = Flask(__name__)

# Connect to PostgreSQL using psycopg2
def get_db_connection():
    try:
        conn = psycopg2.connect(
            dbname=Config.DATABASE_CONFIG['database'],
            user=Config.DATABASE_CONFIG['user'],
            password=Config.DATABASE_CONFIG['password'],
            host=Config.DATABASE_CONFIG['host'],
            port=Config.DATABASE_CONFIG['port']
        )
        return conn
    except psycopg2.Error as e:
        print(f"Error connecting to the database: {e}")
        return None

@app.route('/')
def index():
    # Example of querying the database using psycopg2
    conn = get_db_connection()
    if conn:
        cur = conn.cursor()
        cur.execute('SELECT * FROM books LIMIT 10;')  # Example query
        books = cur.fetchall()
        cur.close()
        conn.close()
        return f"Books: {books}"
    return "Error connecting to the database"

if __name__ == '__main__':
    app.run(debug=True)
