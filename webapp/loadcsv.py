# load.py

import csv
import pymysql
from datetime import datetime
import time
import os

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

def load_csv_into_teams(csv_file_path, num_entries = None ):
    start_time = time.time()  # Record the start time

    with open(csv_file_path, 'r') as file:
        reader = csv.reader(file)
        next(reader)
        teams_data = [(int(row[0]), row[1]) for row in reader][:num_entries]

    with connection.cursor() as cursor:
        cursor.executemany('INSERT INTO teams (team_id, team_name) VALUES (%s, %s)', teams_data)

    connection.commit()

    end_time = time.time()  # Record the end time
    time_taken = end_time - start_time  # Calculate the time taken

    return f"{len(teams_data)} Teams loaded from CSV in {time_taken:.2f} seconds"

def load_csv_into_match_data(csv_file_path, num_entries = None):
    start_time = time.time()

    with open(csv_file_path, 'r') as file:
        reader = csv.reader(file)
        next(reader)
        match_data = [
            (int(row[0]), int(row[1]), int(row[2]), int(row[3]), int(row[4]), int(row[5])) for row in reader
        ][:num_entries]

    with connection.cursor() as cursor:
        cursor.executemany('''
            INSERT INTO match_data (Match_ID, TeamA_id, TeamB_id, Score_A, Score_B, Wining_Team)
            VALUES (%s, %s, %s, %s, %s, %s)
        ''', match_data)

    connection.commit()

    end_time = time.time()  # Record the end time
    time_taken = end_time - start_time  # Calculate the time taken

    return f"{len(match_data)} Matches loaded from CSV in {time_taken:.2f} seconds"
