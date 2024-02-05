# app.py

from flask import Flask, render_template, request, jsonify ,render_template_string
import tablecreator
import showtables
import showdata
import deletetables
import deletedata
from loadcsv import load_csv_into_teams, load_csv_into_match_data
import os
from datetime import datetime
import time


app = Flask(__name__)



@app.route('/')
def home():
    return render_template('index.html')

@app.route('/create-tables')
def create_tables_route():
    tablecreator.create_tables()
    return 'Tables created successfully!'

@app.route('/show-tables')
def show_tables_route():
    return showtables.show_tables()

@app.route('/delete-tables')
def delete_tables_route():
    return deletetables.delete_tables()

@app.route('/load-data/<num_entries>', methods=['POST'])
def load_data(num_entries):
    if num_entries == 'full':
        num_entries =  11521
    else:
        num_entries = int(num_entries)

    start_time = time.time()

    teams_result = load_csv_into_teams(os.path.join(os.getcwd(), 'cwcteams.csv'), num_entries)
    matches_result = load_csv_into_match_data(os.path.join(os.getcwd(), 'cwcmatch.csv'), num_entries)

    end_time = time.time()

    time_taken = end_time - start_time


    message = f'''
              <h2>Load Data Summary</h2>
              <p>Teams loaded successfully: <strong>{teams_result}</strong></p>
              <p>Matches loaded successfully: <strong>{matches_result}</strong></p>
              <p>Time taken: <strong>{time_taken:.2f} seconds</strong> to load {num_entries} entries</p>
          '''
    return render_template_string(message)

@app.route('/show-teams')
def show_teams_route():
    teams_data = showdata.show_teams()
    print(teams_data)
    return render_template('show_teams.html', teams_data=teams_data)

@app.route('/show-match-data')
def show_match_data_route():
    match_data = showdata.show_match_data()
    return render_template('show_match_data.html', match_data=match_data)

@app.route('/show-matches-for-team', methods=['POST'])
def show_matches_for_team():
    team_id = request.form.get('team_id')


    matches_data, matches_won_count = showdata.show_matches_for_team(team_id)

    return render_template('show_matches_for_team.html', matches_data=matches_data, matches_won_count=matches_won_count)

@app.route('/delete-data' , methods = ['POST'])
def delete_data_route():
    deletedata.delete_data()
    return 'Data deleted successfully!'



app.secret_key = 'your_secret_key_here'

if __name__ == '__main__':
    app.run(debug=True)
