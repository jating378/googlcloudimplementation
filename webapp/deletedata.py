

import pymysql
from flask import redirect, url_for

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

def delete_data():


    with connection.cursor() as cursor:

        cursor.execute('DELETE FROM match_data')
        cursor.execute('DELETE FROM teams')

    connection.commit()


    return redirect(url_for('show_tables_route'))

