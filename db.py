# db.py

import psycopg2
from psycopg2.extras import RealDictCursor

def get_db_connection():
    conn = psycopg2.connect(
        dbname="trackter_db",
        user="postgres",
        password="Nishanthi29@10",
        host="localhost",
        port="5432"
    )
    return conn
