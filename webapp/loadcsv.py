

import csv
import pymysql
from flask import Flask, request, render_template, jsonify
from datetime import datetime

app = Flask(__name__)

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

def load_csv_into_teams(csv_file_path):
    with open(csv_file_path, 'r') as file:
        reader = csv.reader(file)
        next(reader)
        teams_data = [(int(row[0]), row[1]) for row in reader]

    with connection.cursor() as cursor:
        cursor.executemany('INSERT INTO teams (team_id, team_name) VALUES (%s, %s)', teams_data)

    connection.commit()
    return f"{len(teams_data)} Teams loaded from CSV"

def load_csv_into_match_data(csv_file_path):
    with open(csv_file_path, 'r') as file:
        reader = csv.reader(file)
        next(reader)
        match_data = [
            (int(row[0]), int(row[1]), int(row[2]), int(row[3]), int(row[4]), int(row[5])) for row in reader
        ]

    with connection.cursor() as cursor:
        cursor.executemany('''
            INSERT INTO match_data (Match_ID, TeamA_id, TeamB_id, Score_A, Score_B, Wining_Team)
            VALUES (%s, %s, %s, %s, %s, %s)
        ''', match_data)

    connection.commit()
    return f"{len(match_data)} Matches loaded from CSV"


if __name__ == '__main__':
    app.run(debug=True)
