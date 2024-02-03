# webapp/showtables.py

import pymysql
from flask import render_template


def show_tables():
    # Cloud SQL Proxy connection configuration
    cloud_sql_connection = {
        'host': '127.0.0.1',  # Cloud SQL Proxy host
        'port': 1234,  # Cloud SQL Proxy port
        'user': 'jating378',
        'password': 'lion54321',
        'db': 'cricketwc',
        'charset': 'utf8mb4',
        'cursorclass': pymysql.cursors.DictCursor,
    }

    # Initialize database connection
    connection = pymysql.connect(**cloud_sql_connection)

    # Fetch table names
    query = "SHOW TABLES"

    with connection.cursor() as cursor:
        cursor.execute(query)
        tables = cursor.fetchall()

    return render_template('showtables.html', tables=tables)
