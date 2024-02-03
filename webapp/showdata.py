
import json
import pymysql
from flask import jsonify
from flask import render_template  # Ensure this line is present

def show_teams():
    cloud_sql_connection = {
        'host': '127.0.0.1',
        'port': 1234,
        'user': 'jating378',
        'password': 'lion54321',
        'db': 'cricketwc',
        'charset': 'utf8mb4',
        'cursorclass': pymysql.cursors.DictCursor,
    }

    connection = pymysql.connect(**cloud_sql_connection)

    try:
        with connection.cursor() as cursor:
            cursor.execute('SELECT * FROM teams')
            teams = cursor.fetchall()

        return teams

    except Exception as e:
        return f"Error fetching teams: {e}"

    finally:
        connection.close()

def show_match_data():
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

    try:
        with connection.cursor() as cursor:
            cursor.execute('''
                SELECT
                    match_data.match_id,
                    teamsA.team_name AS TeamA_name,
                    teamsB.team_name AS TeamB_name,
                    match_data.Score_A,
                    match_data.Score_B,
                    teamsW.team_name AS Wining_Team
                FROM
                    match_data
                INNER JOIN
                    teams AS teamsA ON match_data.TeamA_id = teamsA.team_id
                INNER JOIN
                    teams AS teamsB ON match_data.TeamB_id = teamsB.team_id
                LEFT JOIN
                    teams AS teamsW ON match_data.Wining_Team = teamsW.team_id
            ''')

            match_data = cursor.fetchall()

        return match_data

    except Exception as e:
        return {'error': f"Error fetching match data: {e}"}

    finally:
        connection.close()

def show_matches_for_team(team_id):
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

    try:
        with connection.cursor() as cursor:
            cursor.execute('''
                SELECT
                    match_data.match_id,
                    teamsA.team_name AS TeamA_name,
                    teamsB.team_name AS TeamB_name,
                    match_data.Score_A,
                    match_data.Score_B,
                    teamsW.team_name AS Wining_Team
                FROM
                    match_data
                INNER JOIN
                    teams AS teamsA ON match_data.TeamA_id = teamsA.team_id
                INNER JOIN
                    teams AS teamsB ON match_data.TeamB_id = teamsB.team_id
                LEFT JOIN
                    teams AS teamsW ON match_data.Wining_Team = teamsW.team_id
                WHERE
                    teamsA.team_id = %s OR teamsB.team_id = %s
            ''', (team_id, team_id))

            match_data = cursor.fetchall()

            # Count the matches won by the selected team
            cursor.execute('''
                SELECT COUNT(*) AS matches_won_count
                FROM match_data
                WHERE Wining_Team = %s
            ''', (team_id,))

            matches_won_count = cursor.fetchone()['matches_won_count']



        return match_data, matches_won_count

    except Exception as e:
        return {'error': f"Error fetching match data: {e}"}, 0

    finally:
        connection.close()
