# createtables.py

import pymysql

def create_tables():
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
            # Create 'teams' table
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS teams (
                    team_id INT AUTO_INCREMENT PRIMARY KEY,
                    team_name VARCHAR(255) NOT NULL
                )
            ''')

            # Create 'match_data' table
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS match_data (
                    match_id INT AUTO_INCREMENT PRIMARY KEY,
                    TeamA_id INT,
                    TeamB_id INT,
                    Score_A INT,
                    Score_B INT,
                    Wining_Team VARCHAR(255),
                    FOREIGN KEY (TeamA_id) REFERENCES teams(team_id),
                    FOREIGN KEY (TeamB_id) REFERENCES teams(team_id)
                )
            ''')

        print("Tables created successfully!")

    except Exception as e:
        print(f"Error creating tables: {e}")

    finally:
        connection.close()

if __name__ == "__main__":
    create_tables()
