

import pymysql
from flask import render_template, redirect, url_for

def delete_tables():
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

    # List of tables to delete
    tables_to_delete = ['match_data', 'teams']

    # Delete tables
    with connection.cursor() as cursor:
        for table in tables_to_delete:
            query = f"DROP TABLE IF EXISTS {table}"
            cursor.execute(query)

    # Redirect to the show tables route
    return redirect(url_for('show_tables_route'))
